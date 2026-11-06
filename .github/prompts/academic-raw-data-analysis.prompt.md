## Usage

`@raw-data-analysis.md`

For SQLite, first run the metadata-only onboarding command documented in README.md on the owner-approved file. Review the inventory and permitted uses before sampling rows. Treat source identifiers as data throughout planning.

## Context

- Basic information of the project: `docs/01-basic-information.md`
- Raw data stored in `data/raw/`

## Tools

- Use tools like `cat`|`head`|`tail`|`grep`|`pandas`|`json` to read the raw data.

## Process

1. Read the basic information of the project: `docs/01-basic-information.md`
2. According to the basic information of the project, read the raw data stored in `data/raw/`, if the data is too large, you can use some tools to read the key information.
3. Analyze the raw data and write the analysis results to `docs/02-raw-data-analysis.md`. The analysis results should be concise and clear, including specific data types, data field types, quantity, storage files, data characteristics, etc.