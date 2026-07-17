# Reproducibility

Run:

```bash
python scripts/validate_counts.py
```

Expected core checks:

- 39 unique core studies;
- roles: 19 attack/failure, 12 defence/system, 8 benchmark;
- publication maturity: 30 preprints, 8 peer-reviewed, 1 peer-reviewed workshop;
- explicit capability counts: provenance 6, attribution 8, causal reconstruction 9, blast radius 7, recovery 7;
- non-benchmark explicit counts: 6, 7, 7, 6, 5;
- peer-reviewed plus workshop subset explicit counts: 1 for each capability.

The validation script exits with a non-zero status if any expected value changes. If the corpus is intentionally revised, update both the data and the explicit expected values in the script, and document the change in `CHANGELOG.md`.
