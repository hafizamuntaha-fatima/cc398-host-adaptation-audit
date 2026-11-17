# CC398 Genomic Features and Host Association

**Hafiza Muntaha Fatima**  
Independent computational reanalysis of published isolate-level data

This project examines three mobile genetic element annotations and eight resistance or immune-evasion gene calls in *Staphylococcus aureus* CC398. It reproduces an initial descriptive analysis, reconciles isolate identifiers across three official source workbooks, and documents differences between annotation columns and the published article.

**Original article:** Matuszewska M, Murray GGR et al. (2022). *Stable antibiotic resistance and rapid human adaptation in livestock-associated MRSA.* eLife 11:e74819. https://doi.org/10.7554/eLife.74819

## Analysis and reproducibility

Open [`notebooks/CC398_Host_Associated_Genomic_Variation_Source_Audited.ipynb`](notebooks/CC398_Host_Associated_Genomic_Variation_Source_Audited.ipynb) in Google Colab and select **Runtime > Run all**. The notebook downloads source files if absent. For a fully offline repeat run, place these three original workbooks in `data/` (already included in this review package):

- `elife-74819-supp1-v1.xlsx` (isolate metadata and accessions)
- `elife-74819-supp3-v1.xls` (clade and mobile element annotations)
- `elife-74819-supp7-v1.xls` (resistance gene calls)

The Python dependencies are listed in `requirements.txt`. The notebook exports tables, charts and input hashes to `results_reconciled/` when executed; the verified Colab exports are provided in [`results/`](results/).

## Summary of the source audit

- The source tables contain **1,180** unique isolates: **704** livestock-associated (LA) and **476** human-associated (HA) evolutionary-clade assignments.
- The strain spellings `7-1`/`07-1` and `7-3`/`07-3` were reconciled without deleting or duplicating any isolate. [`isolate_id_reconciliation.csv`](results/isolate_id_reconciliation.csv) records the changes.
- All **22** checks of the earlier **1,178-isolate** descriptive results pass against a reproduced historical subset. The corrected full-cohort percentages sometimes differ because two records have been restored.
- Input file SHA-256 hashes are recorded in [`input_manifest.csv`](results/input_manifest.csv) and match the original eLife workbooks.
- Six metadata records lack individual accession identifiers; their available BioProject information is retained. See [`accession_gaps.csv`](results/accession_gaps.csv).
- Among the 1,180 paired gene calls, **five** `mecA` calls differ between Supplementary files 3 and 7. The eight-gene chart uses the explicit column provenance shown in the notebook.

## Interpretation boundary

The `Sa3` binary annotation in Supplementary file 3 is positive in **109/704 LA isolates (15.5%)**. The article text reports **68/704 (9.7%)** LA isolates with a φSa3 prophage. These figures are not interchangeable without a validated annotation-definition mapping. The project deliberately reports both and does not force them into agreement.

The eight two-sided Fisher exact tests are **pooled, isolate-level descriptive comparisons**, not phylogenetically independent tests. They do not establish repeated acquisitions or host-specific adaptation. The published study separately analyses **70 phylogenetically independent mixed-host groups** using McNemar tests. Reproducing that analysis would require the relevant phylogenetic grouping and an explicitly matched comparison design.

## Repository contents

| Location | Contents |
|---|---|
| `notebooks/` | Google Colab notebook with source validation, plots and statistical analysis |
| `data/` | Unmodified original workbooks from the cited paper |
| `results/` | Result tables, isolates and accessions, source concordance audit, and figures |
| `checks/` | Lightweight integrity validation of packaged source files and reports |

Source data and original published findings are credited to Matuszewska, Murray and coauthors. This project is a reanalysis of publicly released annotations, not an independent replication of the complete evolutionary inference.
