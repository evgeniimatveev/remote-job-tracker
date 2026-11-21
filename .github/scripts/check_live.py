"""Run after `python main.py` against the live Arbeitnow API: did the pipeline really produce a snapshot?

The fetcher swallows network errors and returns an empty list, so a broken API would otherwise look like a
successful run. This script turns that into a failure.
"""
import csv
import json
import os
import sys

problems = []
with open("data/raw/arbeitnow_raw.json", encoding="utf-8") as fh:
    raw = json.load(fh)
if not raw:
    problems.append("the API returned no listings (or the request failed)")
NEEDED = ["title", "company_name", "location", "url", "remote", "created_at"]
for key in NEEDED:
    missing = sum(1 for j in raw if key not in j)
    if missing:
        problems.append(f"field '{key}' is missing in {missing} of {len(raw)} listings")
bad_url = sum(1 for j in raw if not str(j.get("url", "")).startswith("http"))
if bad_url:
    problems.append(f"{bad_url} listings have no http url")

with open("data/processed/jobs_clean.csv", encoding="utf-8-sig", newline="") as fh:
    rows = list(csv.DictReader(fh))
if len(rows) != len(raw):
    problems.append(f"CSV has {len(rows)} rows, raw JSON {len(raw)} listings")
if rows and list(rows[0].keys()) != ["title", "company", "location", "url"]:
    problems.append(f"CSV columns are {list(rows[0].keys())}")

summary = f"{len(raw)} live listings, {sum(1 for j in raw if j.get('remote'))} remote, {len({j.get('company_name') for j in raw})} companies"
print("Live run:", summary, "|", len(problems), "problem(s)")
for p in problems:
    print("FAIL ", p)
path = os.environ.get("GITHUB_STEP_SUMMARY")
if path:
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(f"## Live Arbeitnow run\n\n{summary}\n\n" + ("✅ all checks passed\n" if not problems else "\n".join(f"- ❌ {p}" for p in problems) + "\n"))
sys.exit(1 if problems else 0)
