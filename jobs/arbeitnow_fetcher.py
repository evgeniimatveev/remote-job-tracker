import requests
import os
import json

def fetch_arbeitnow_jobs(query="data analyst"):
    url = "https://www.arbeitnow.com/api/job-board-api"
    jobs = []

    try:
        print(f"[INFO] Fetching jobs from: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        all_jobs = data.get("data", [])

        # 🔍 Manual keyword filtering
        jobs = [
            job for job in all_jobs
            if query.lower() in job.get("title", "").lower()
        ]

        # 💾 Save raw data
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/arbeitnow_raw.json", "w", encoding="utf-8") as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2)

        print(f"[INFO] Extracted {len(jobs)} job(s) for keyword '{query}'")
        return jobs

    except Exception as e:
        print(f"[ERROR] Failed to fetch jobs from Arbeitnow: {e}")
        return []