from jobs.arbeitnow_fetcher import fetch_arbeitnow_jobs
from jobs.exporter import save_to_csv
import json

def main():
    print("[🚀] Fetching jobs from Arbeitnow...")
    jobs = fetch_arbeitnow_jobs(query="")

    print(f"[INFO] Extracted {len(jobs)} job entries")

    if jobs:
        # 🎯 Clean version
        jobs_simple = [
            {
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "url": job.get("url")
            }
            for job in jobs
        ]

        print("[INFO] First job preview:")
        print(json.dumps(jobs_simple[0], indent=2, ensure_ascii=False))

        save_to_csv(jobs_simple, filename="data/processed/jobs_clean.csv")
        print("[✅] Saved cleaned jobs to: data/processed/jobs_clean.csv")

    else:
        print("[⚠️] No jobs found!")

if __name__ == "__main__":
    main()