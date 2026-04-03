# Germany Remote Job Tracker (May 2025)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Tableau](https://img.shields.io/badge/Tableau-Story-blueviolet?logo=tableau)
![ETL](https://img.shields.io/badge/ETL-Pipeline-orange)
![API](https://img.shields.io/badge/API-Arbeitnow-green)
![Data](https://img.shields.io/badge/Data-JSON→CSV-yellow)
![Automation](https://img.shields.io/badge/Automation-Enabled-purple)
![Storytelling](https://img.shields.io/badge/Data-Storytelling-blue)
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
│  ├──tableau//storytelling_reports/ ← PDF Story Slides
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
## 📊 Tableau Storytelling Reports

Explore structured visual insights generated from real-time job data using Python + Tableau:

### 📘 Story 1 — Overview & Methodology
[Tech Job Trends in May 2025](https://github.com/evgeniimatveev/remote-job-tracker/blob/main/dashboards/tableau/storytelling_reports/Tech%20Job%20Trends%20in%20May%202025.pdf)

_Project introduction, data pipeline, and overall hiring landscape._

---

### 🏢 Story 2 — Top Hiring Companies
[Top Hiring Companies](https://github.com/evgeniimatveev/remote-job-tracker/blob/main/dashboards/tableau/storytelling_reports/Top%20Hiring%20Companies.pdf)

_Key Insight:_  
MY Humancapital GmbH dominates the dataset, accounting for nearly half of all listings.

_Interpretation:_  
This suggests either aggressive hiring or centralized job aggregation.

---

### 🌍 Story 3 — Job Locations in Germany
[Where Are the Jobs Located?](https://github.com/evgeniimatveev/remote-job-tracker/blob/main/dashboards/tableau/storytelling_reports/Where%20Are%20the%20Jobs%20Located_.pdf)

_Key Insight:_  
Munich leads by a wide margin, followed by Berlin, Hamburg, and Karlsruhe.

_Interpretation:_  
Remote-friendly tech hiring is concentrated in major German tech hubs.

---

### 💼 Story 4 — Roles in Demand
[What Roles Are in Demand?](https://github.com/evgeniimatveev/remote-job-tracker/blob/main/dashboards/tableau/storytelling_reports/What%20Roles%20Are%20in%20Demand_.pdf)

_Key Insight:_  
Software, IT support, and finance roles appear most frequently.

_Interpretation:_  
Demand spans both technical and business-oriented positions.

---

> 💡 All reports are generated from live API data and can be refreshed via the ETL pipeline.


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

**Python 3.11 + requests, json, os**

**Tableau Public Story**

**VS Code + GitHub**

**Arbeitnow Job API**




## 📢 Stay Connected!  
💻 **GitHub Repository:** [Evgenii Matveev](https://github.com/evgeniimatveev)  
🌐 **Portfolio:** [Data Science Portfolio](https://www.datascienceportfol.io/evgeniimatveevusa)  
📌 **LinkedIn:** [Evgenii Matveev](https://www.linkedin.com/in/evgenii-matveev-510926276/)  
