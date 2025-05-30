# 🇩🇪 Germany Remote Job Tracker (May 2025)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Tableau](https://img.shields.io/badge/Tableau-Story-blueviolet?logo=tableau)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

This project automates the collection and visualization of **remote-friendly tech jobs in Germany**  
using the [Arbeitnow Job API](https://www.arbeitnow.com/api/job-board-api).  
It includes a clean **ETL pipeline** and an interactive **Tableau story** to highlight key hiring trends.

---

## 🚀 Features

🔄 **Live ETL Pipeline** (JSON → CSV)  
🔎 **Filters job data** with Python (company, location, title)  
📦 **Structured outputs**: raw `.json` + clean `.csv`  
📊 **Tableau Story** — top employers, cities, job roles  
🖱️ **Interactive visual storytelling**  
✅ **Rerunnable** in seconds to update snapshots

---
```bash
## 🧱 Project Structure

mlops_job_project/
│
├── data/
│ ├── raw/ ← Raw API output (arbeitnow_raw.json)
│ └── processed/ ← Clean CSV for Tableau (jobs_clean.csv)
│
├── dashboards/
│ └── tableau/ ← .twb file with full story
│
├── jobs/
│ ├── arbeitnow_fetcher.py ← API pull logic
│ ├── exporter.py ← JSON & CSV writer
│
├── main.py ← Main script: fetch → clean → export
├── requirements.txt ← Python packages
└── README.md ← You are here!

```
---

## 🧠 Tableau Story Highlights

| 📌 Topic              | Insights                                               |
|----------------------|--------------------------------------------------------|
| 🏢 **Top Employers**   | One company (MY Humancapital GmbH) posted ~50% jobs   |
| 🌍 **Top Locations**   | Munich, Berlin, Hamburg lead in remote hiring         |
| 💼 **Top Job Titles**  | Softwareentwickler, IT-Support, Finance Manager       |

> ✅ All visualizations are based on real-time public API data and can be refreshed at any time.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/mlops_job_project.git
cd mlops_job_project

# (Optional) create a virtual environment
conda create -n job_env python=3.11 -y
conda activate job_env

# Install requirements
pip install -r requirements.txt

# Run the full flow
python main.py
```
📎 Tech Stack
Python 3.11 + requests, json, os

Tableau Public Story

VS Code + GitHub

Arbeitnow Job API

🎯 Use Case
Perfect for:

Showcasing ETL + BI skills

Practicing API integration + automated data cleaning

Visual storytelling for tech hiring insights

Adding a portfolio-ready project to GitHub or LinkedIn


## 📢 Stay Connected!  
💻 **GitHub Repository:** [Evgenii Matveev](https://github.com/evgeniimatveev)  
🌐 **Portfolio:** [Data Science Portfolio](https://www.datascienceportfol.io/evgeniimatveevusa)  
📌 **LinkedIn:** [Evgenii Matveev](https://www.linkedin.com/in/evgenii-matveev-510926276/)  
