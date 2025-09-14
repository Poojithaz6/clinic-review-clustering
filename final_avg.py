import pandas as pd

# Load the cleaned file (use .csv or .xlsx as applicable)
df = pd.read_csv("regular_visits1.csv")  # or use read_excel() if it's .xlsx

# Group by Patient to count visits and calculate total & average spending
summary = df.groupby(['Patient File No', 'Patient Name']).agg({
    'Total Paid Amt': ['count', 'sum', 'mean']
}).reset_index()

# Rename columns
summary.columns = ['Patient File No', 'Patient Name', 'Number of Visits', 'Total Spent', 'Average Spent per Visit']

# Save to a new file
summary.to_csv("patient_spending_summary.csv", index=False)

print("✅ Done! File saved as 'patient_spending_summary.csv'")
