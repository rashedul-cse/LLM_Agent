# Reproducibility

Run:

```bash
python scripts/validate_counts.py
```

Expected checks:

- candidate map: 86 records;
- usable full texts: 79;
- adjacent/background sources: 36;
- core corpus: 43 unique studies;
- roles: 21 attack/failure, 14 defence/system, 8 benchmark;
- publication maturity: 34 preprints, 8 peer-reviewed papers, 1 workshop paper;
- explicit capability counts: provenance 7, attribution 10, causal reconstruction 11, blast radius 9, recovery 7;
- non-benchmark explicit counts: 7, 9, 9, 8, 5;
- peer-reviewed-only subset explicit counts: 1 for each capability;
- four master-to-manuscript ID crosswalk rows.

The validation script exits with a non-zero status if an expected value changes. If the corpus is intentionally revised, update the data, the explicit expected values in the script, and `docs/CHANGELOG.md`.
