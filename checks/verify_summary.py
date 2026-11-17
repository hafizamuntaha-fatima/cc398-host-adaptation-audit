"""Verify source hashes and summaries after downloading the original workbooks."""
from pathlib import Path
import csv
import hashlib

root = Path(__file__).resolve().parents[1]
data = root / "data"
results = root / "results"
with (results / "input_manifest.csv").open(newline="", encoding="utf-8") as f:
    manifest = list(csv.DictReader(f))
for item in manifest:
    path = data / item["filename"]
    if not path.exists():
        print(f"Source absent locally: {path.name}. Run the notebook to retrieve it.")
        continue
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
with (results / "cohort_audit.csv").open(newline="", encoding="utf-8") as f:
    cohort = list(csv.DictReader(f))
assert len(cohort) == 3
assert all(int(row["matched_ids"]) == 1180 for row in cohort)
with (results / "source_gene_concordance.csv").open(newline="", encoding="utf-8") as f:
    concordance = {r["gene"]: int(r["discordant_calls"]) for r in csv.DictReader(f)}
assert concordance == {"mecA": 5, "scn": 0, "sak": 0, "chs": 0}
print("Summary integrity checks: PASS")
