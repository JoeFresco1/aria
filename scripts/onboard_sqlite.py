"""Capture declared SQLite metadata as a portable ARIA workspace source record."""

import argparse
import json
import re
import sqlite3
import sys
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path


def open_source(path: Path) -> sqlite3.Connection:
    """Open an existing file for read-only inspection of its main database."""
    uri = path.resolve(strict=True).as_uri() + "?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA trusted_schema = OFF")
    connection.execute("PRAGMA query_only = ON")
    return connection


def build_workspace(path: Path, source_id: str) -> dict:
    """Read a single consistent schema snapshot without querying application rows."""
    if not re.fullmatch(r"[a-z][a-z0-9_-]*", source_id):
        raise ValueError("Use a lowercase source ID starting with a letter.")
    inventory = []
    with closing(open_source(path)) as connection:
        connection.execute("BEGIN")
        objects = connection.execute(
            "SELECT name, type FROM pragma_table_list "
            "WHERE schema = 'main' AND lower(substr(name, 1, 7)) <> 'sqlite_' ORDER BY name"
        )
        for obj in objects:
            entry = dict(obj)
            # Resolving views or virtual tables can invoke extension code.
            if entry["type"] == "table":
                entry["columns"] = [dict(row) for row in connection.execute(
                    'SELECT name, type AS declared_type, pk AS primary_key_position, '
                    'hidden AS column_kind FROM pragma_table_xinfo(?, ?)', (entry["name"], "main")
                )]
                entry["foreign_keys"] = [dict(row) for row in connection.execute(
                    "SELECT * FROM pragma_foreign_key_list(?, ?)", (entry["name"], "main")
                )]
            else:
                entry["inspection"] = "name and object type only"
            inventory.append(entry)
    ref = f"#/records/{source_id}"
    record = {
        "kind": "source", "version": 1,
        "description": f"SQLite metadata for {source_id}",
        "connection_ref": f"sqlite:{source_id}",
        "inventory_ref": f"{ref}/inventory", "skill_ref": f"{ref}/connection_skill",
        "inspected_at": datetime.now(UTC).isoformat(),
        "provenance": "database-declared metadata",
        "inventory": inventory,
        "connection_skill": {
            "binding": "Ask the source owner to bind the logical ID to an approved local database file.",
            "inspection": "Run scripts/onboard_sqlite.py with the approved file and this source ID.",
            "access": "The inspection connection opens the main database with mode=ro.",
            "review": "Confirm business grain, join cardinality, sampling and export permissions with the owner.",
        },
    }
    return {"format": "aria-study/v1", "records": {source_id: record}}


def main() -> int:
    """Write a new workspace document, preserving any existing output file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    parser.add_argument("source_id")
    parser.add_argument("output", type=Path, help="new JSON file")
    args = parser.parse_args()
    try:
        document = json.dumps(build_workspace(args.database, args.source_id), indent=2)
        with args.output.open("x", encoding="utf-8") as output:
            output.write(document + "\n")
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"Onboarding failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
