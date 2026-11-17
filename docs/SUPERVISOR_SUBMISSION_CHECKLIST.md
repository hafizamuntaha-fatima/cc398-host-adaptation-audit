# Supervisor submission evidence checklist

This checklist maps the questions in Dr. Marta Matuszewska's email of 16 November 2026 to inspectable materials in this repository. It is a project quality-control record, not a manuscript or an email.

| Requested item | Evidence | Status |
|---|---|---|
| Python code / Google Colab notebook | [Editable notebook](../notebooks/CC398_Host_Associated_Genomic_Variation_Source_Audited.ipynb), [executed notebook](../notebooks/CC398_Executed.ipynb) | Available; GitHub Actions execution passed |
| Input files or accession list | [Official file manifest](../results/input_manifest.csv), [isolate-accession manifest](../results/isolate_accession_manifest.csv) | 1,180 isolate rows; 6 individual accession fields are unavailable in the published metadata |
| Definitions of the two groups | [Methods](METHODS.md), [cohort audit](../results/cohort_audit.csv) | LA and HA refer to the published evolutionary clades, not directly to sampled host |
| Missing annotations and exclusions | [Cohort audit](../results/cohort_audit.csv), [identifier reconciliation](../results/isolate_id_reconciliation.csv), [accession gaps](../results/accession_gaps.csv) | Two strain-ID spelling inconsistencies reconciled; feature-level denominators documented |
| Source of p-values | [Fisher test table](../results/gene_fisher_unadjusted.csv), notebook statistical section | Unadjusted two-sided isolate-level Fisher exact tests; not phylogenetically independent |
| Figures with consistent group colours | [MGE plot](../figures/figure_02_mobile_elements.png), [gene plot](../figures/figure_03_genes.png) | LA dark blue, HA orange across both figures |
| Reproducible re-execution | [Workflow](../.github/workflows/reproduce-cc398.yml), [verification script](../scripts/verify_results.py) | Successful workflow, original workbooks downloaded and hashes verified |

## Specific scientific interpretation limits

- The earlier figure came from a 1,178-isolate intersection. The reconciled original-source cohort contains 1,180 isolates (704 LA, 476 HA). The [historical comparison](../results/earlier_summary_comparison.csv) records 22 matches to the earlier subset; this does not imply that every full-cohort percentage is identical to the original email.
- Supplementary File 3 contains 109 LA isolates positive for its `Sa3` field, whereas the paper reports 68 LA isolates carrying a φSa3 prophage. The source-field definition and the manuscript's element-level definition have not been established as equivalent. See [direct comparison](../results/sa3_annotation_vs_article.csv). Do not present these as the same count.
- Supplementary Files 3 and 7 differ on five `mecA` calls. See [source concordance](../results/source_gene_concordance.csv) and [individual differences](../results/source_gene_disagreements.csv).
- The original study's evidence for evolutionary dynamics and adaptation uses phylogenetic analysis, including 70 independent mixed-host groups. Pooled Fisher tests do not reproduce its McNemar analyses or establish independent acquisitions.
- The original source workbooks are available through the file URLs in the manifest. Their hashes were verified against the inputs retrieved by the successful workflow.
- This analysis is a reanalysis of published annotations. It is not a replication of the original study's phylogenetic reconstructions or a claim of new experimental findings.

## Before sharing with Dr. Matuszewska

1. Open the [executed notebook](../notebooks/CC398_Executed.ipynb) and review its outputs.
2. Ensure the original sent figure and the updated 1,180-isolate figure are not described as numerically identical.
3. Explicitly acknowledge the phylogenetic limitation and the unresolved `Sa3` definition difference in accompanying correspondence.
4. Provide the repository link and point directly to the executed notebook, accession manifest, and method documentation.
5. Share the correspondence only after the applicant reviews and approves its wording.
