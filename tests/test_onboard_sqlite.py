"""Exercise source onboarding against a disposable database."""

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

from scripts.onboard_sqlite import open_source


class OnboardingTests(unittest.TestCase):
    def test_read_only_inventory_and_retry(self) -> None:
        """Inventory preserves declared keys, avoids rows, and protects existing output."""
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            db = base / "private #1.sqlite"
            out = base / "workspace.json"
            with closing(sqlite3.connect(db)) as connection:
                connection.executescript("""
                    CREATE TABLE account(id INTEGER PRIMARY KEY, label TEXT);
                    CREATE TABLE payment(account REFERENCES account(id));
                    CREATE VIEW labels AS SELECT label FROM account;
                    INSERT INTO account VALUES (1, 'private-row-value');
                """)
            with closing(open_source(db)) as connection:
                with self.assertRaises(sqlite3.OperationalError):
                    connection.execute("DELETE FROM account")
            args = [sys.executable, "scripts/onboard_sqlite.py", str(db), "billing", str(out)]
            subprocess.run(args, check=True)
            snapshot = out.read_text(encoding="utf-8")
            inventory = json.loads(snapshot)["records"]["billing"]["inventory"]
            self.assertEqual(inventory[0]["columns"][0]["primary_key_position"], 1)
            self.assertEqual(inventory[1]["type"], "view")
            self.assertEqual(inventory[2]["foreign_keys"][0]["table"], "account")
            self.assertNotIn(db.name, snapshot)
            self.assertNotIn("private-row-value", snapshot)
            self.assertNotEqual(subprocess.run(args, capture_output=True).returncode, 0)
            self.assertEqual(snapshot, out.read_text(encoding="utf-8"))
            missing = base / "absent.sqlite"
            with self.assertRaises(FileNotFoundError):
                open_source(missing)
            self.assertFalse(missing.exists())
