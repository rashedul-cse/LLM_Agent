# Deposit Readiness Checklist

## Ready

- [x] Core study-level extraction exported as CSV.
- [x] Adjacent literature exported.
- [x] Appendix A census exported.
- [x] Capability counts and role breakdown exported.
- [x] Sensitivity values exported.
- [x] Search and screening source workbooks preserved.
- [x] Codebook and data dictionary included.
- [x] Reproducibility script included.
- [x] Citation and Zenodo metadata templates included.
- [x] Copyrighted full-text PDFs excluded.
- [x] Checksums and file manifest generated.

## Must be completed before the manuscript claims full auditability

- [ ] Deposit the repository and insert the assigned DOI in `README.md`, `CITATION.cff`, and `metadata/zenodo.json`.
- [ ] Complete any missing database execution dates and raw hit counts from original export records.
- [ ] Verify changing 2026 bibliographic metadata.
- [ ] Verify the provisional three-study MEIRC mapping against exact paper pages/tables.
- [ ] Add genuine second-coder labels and agreement statistics only if independently completed.

## Suggested Zenodo upload process

1. Create a new Zenodo deposition.
2. Upload the repository ZIP.
3. Use the metadata in `metadata/zenodo.json`.
4. Reserve a DOI, update the repository metadata files, regenerate the ZIP, and upload the revised archive.
5. Publish the deposition.
6. Cite the final resolving DOI in the manuscript's Data Availability section.
