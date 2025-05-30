import pandas as pd
import os

def save_to_csv(jobs, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False, encoding="utf-8-sig")  # ✅ Unicode-safe
