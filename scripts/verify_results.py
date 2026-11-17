"""Check that reconstructed results agree with the published source cohort."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results_reconciled"

def load(name):
    path = OUT / name
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)

manifest = load("input_manifest.csv")
assert len(manifest) == 3, "Expected three original supplementary workbooks"
import hashlib
for row in manifest.to_dict("records"):
    source = ROOT / "data" / row["filename"]
    assert source.is_file(), f"Missing source workbook: {source}"
    assert hashlib.sha256(source.read_bytes()).hexdigest() == row["sha256"]

cohort = load("cohort_audit.csv")
assert len(cohort) == 3
assert all(cohort["matched_ids"].astype(int) == 1180)
assert all(cohort["unmatched_ids"].astype(int) == 0)

accessions = load("isolate_accession_manifest.csv")
assert len(accessions) == 1180
assert accessions["isolate_id"].nunique() == 1180
assert int(accessions["accession"].isna().sum()) == 6

historical = load("earlier_summary_comparison.csv")
assert len(historical) == 22 and historical["match"].astype(bool).all()

mge = load("mge_prevalence.csv").set_index(["feature", "clade"])
assert int(mge.loc[("Sa3 (S3 annotation)", "LA"), "n_present"]) == 109
assert int(mge.loc[("Sa3 (S3 annotation)", "LA"), "n_observed"]) == 704

concordance = load("source_gene_concordance.csv").set_index("gene")
assert int(concordance.loc["mecA", "discordant_calls"]) == 5

genes = load("gene_prevalence.csv")
assert genes["feature"].nunique() == 8 and len(genes) == 16
stats = load("gene_fisher_unadjusted.csv")
assert len(stats) == 8 and stats["gene"].nunique() == 8

print("PASS: source hashes, 1,180-isolate cohort, accession manifest,")
print("22 historical comparisons, eight genes, five mecA disagreements, and Sa3 annotation.")
