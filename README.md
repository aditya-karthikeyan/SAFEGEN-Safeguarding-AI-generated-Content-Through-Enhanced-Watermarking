# Data Registry

Keep raw, interim, and processed data in the respective folders. Never edit files in `data/raw/`.

## Guidelines
- **Do not** commit private or large raw data to Git. Prefer Git LFS for large, non-sensitive artifacts, or host externally.
- Record each dataset in the table below.

| Alias | Path | Source | License | Rows | Columns | Notes |
|------:|:-----|:-------|:--------|-----:|--------:|:------|
| test_analysis | data/interim/test_analysis.csv | Excel export | TBD | - | - | Converted from the provided spreadsheet |

