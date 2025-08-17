import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data (expects employees.csv in the same directory). If missing, it will synthesize a dataset of 100 rows.
csv_path = 'employees.csv'
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    np.random.seed(42)
    departments = ["IT", "Finance", "HR", "Sales", "Operations", "Marketing"]
    regions = ["North", "South", "East", "West"]
    n = 100
    df = pd.DataFrame({
        "EmployeeID": range(1, n+1),
        "Department": np.random.choice(departments, size=n, p=[0.25, 0.2, 0.15, 0.2, 0.1, 0.1]),
        "Region": np.random.choice(regions, size=n),
        "PerformanceScore": np.random.normal(loc=75, scale=10, size=n).round(1)
    })
    df.to_csv(csv_path, index=False)

# Frequency count for the "IT" department
it_count = int((df["Department"] == "IT").sum())
print(f"IT department count: {it_count}")

# Plot histogram-like bar chart for department distribution
dept_counts = df["Department"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
dept_counts.plot(kind="bar")
plt.title("Department Distribution (n={len(df)})")
plt.xlabel("Department")
plt.ylabel("Count of Employees")
plt.tight_layout()
plt.savefig("department_histogram.png", dpi=150, bbox_inches="tight")
