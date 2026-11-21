"""Static checks, standard library only (nothing is fetched).

* every Python file compiles (warnings are errors) and no .pyc / __pycache__ is tracked
* README links that point into this repository lead to existing files
* the Key Findings in the README are re-computed from the saved snapshot (data/raw, data/processed)
"""
import collections
import csv
import json
import os
import re
import subprocess
import sys
import urllib.parse
import warnings

problems = []
tracked = [t.strip('"') for t in subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True, encoding="utf-8").stdout.splitlines()]

for t in tracked:
    if t.endswith(".pyc") or "__pycache__" in t:
        problems.append(f"{t}: compiled Python file is tracked")
warnings.simplefilter("error", SyntaxWarning)
py = sorted(t for t in tracked if t.endswith(".py"))
for f in py:
    with open(f, encoding="utf-8") as fh:
        try:
            compile(fh.read(), f, "exec")
        except (SyntaxError, SyntaxWarning) as exc:
            problems.append(f"{f}: does not compile: {exc}")

with open("README.md", encoding="utf-8") as fh:
    readme = fh.read()
n_links = 0
for target in re.findall(r"\]\(((?:[^()\s]|\([^)]*\))+)\)", readme):
    m = re.match(r"https://github\.com/evgeniimatveev/remote-job-tracker/(?:blob|tree)/main/(.+)", target)
    if m:
        path = urllib.parse.unquote(m.group(1))
    elif re.match(r"^(https?:|#|mailto:)", target):
        continue
    else:
        path = urllib.parse.unquote(target.split("#")[0])
    n_links += 1
    if path not in tracked and not os.path.exists(path):
        problems.append(f"README: link to a missing file: {path}")

# --- Key Findings, re-computed
with open("data/raw/arbeitnow_raw.json", encoding="utf-8") as fh:
    raw = json.load(fh)
n = len(raw)
comp = collections.Counter(j["company_name"] for j in raw)
loc = collections.Counter(j["location"] for j in raw)
berlin = sum(c for name, c in loc.items() if name.startswith("Berlin"))
remote = sum(1 for j in raw if j["remote"])
top5 = sum(c for _, c in comp.most_common(5))
claims = [
    ("100 listings", n, 100),
    ("top employer", comp.most_common(1)[0][0], "MY Humancapital GmbH"),
    ("top employer has 47 listings", comp.most_common(1)[0][1], 47),
    ("Munich has 36 listings", loc["Munich"], 36),
    ("Berlin (both spellings) is 15%", round(berlin * 100 / n), 15),
    ("Hamburg has 4 listings", loc["Hamburg"], 4),
    ("5 truly remote listings", remote, 5),
    ("top 5 companies hold 72%", round(top5 * 100 / n), 72),
]
for name, got, want in claims:
    if got != want:
        problems.append(f"README figure '{name}': README says {want}, data says {got}")
with open("data/processed/jobs_clean.csv", encoding="utf-8-sig", newline="") as fh:
    rows = list(csv.DictReader(fh))
if len(rows) != n or [r["title"] for r in rows] != [j["title"] for j in raw] or [r["url"] for r in rows] != [j["url"] for j in raw]:
    problems.append("jobs_clean.csv does not match arbeitnow_raw.json (count, titles or urls)")
if list(rows[0].keys()) != ["title", "company", "location", "url"]:
    problems.append(f"jobs_clean.csv columns are {list(rows[0].keys())}")

print(f"Checked {len(py)} Python files, {n_links} README links, {len(claims)} README figures, the CSV against the raw JSON, {len(problems)} problem(s)")
for p in problems:
    print("FAIL ", p)
sys.exit(1 if problems else 0)
