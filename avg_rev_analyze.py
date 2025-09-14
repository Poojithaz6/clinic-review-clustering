import pandas as pd

# Load and clean
df = pd.read_csv("regular_value_patients.csv", na_values=["", " ", "NA", "N/A", "None", "-"])

# Parse dates
df['Bill Date'] = pd.to_datetime(df['Bill Date'], errors='coerce')

# Drop rows with missing essentials
df = df.dropna(subset=['Patient File No', 'Patient Name', 'Bill Date', 'Paid Amt'])

# Create unique visit ID (per patient per day)
df['VisitID'] = df['Patient File No'].astype(str) + "_" + df['Bill Date'].dt.strftime('%Y-%m-%d')

# Collapse multiple bills per day
visit_df = df.groupby('VisitID').agg({
    'Patient File No': 'first',
    'Patient Name': 'first',
    'Bill Date': 'first',
    'Paid Amt': 'sum'
}).reset_index()

# Group by patient to get totals
patient_summary = visit_df.groupby(['Patient File No', 'Patient Name']).agg(
    total_visits=('VisitID', 'count'),
    total_paid=('Paid Amt', 'sum'),
    avg_paid_per_visit=('Paid Amt', 'mean'),
    first_visit=('Bill Date', 'min'),
    last_visit=('Bill Date', 'max')
).reset_index()

# Split based on revenue threshold
high_value = patient_summary[patient_summary['total_paid'] > 10500]
regular_value = patient_summary[patient_summary['total_paid'] <= 10500]

# Save both
high_value.to_csv("high_value_patients.csv", index=False)
regular_value.to_csv("regular_value_patients.csv", index=False)

# Output counts
print(f"✅ High value patients (Paid > 10500): {len(high_value)}")
print(f"✅ Regular value patients: {len(regular_value)}")
print("\n📁 Files saved:")
print("- high_value_patients.csv")
print("- regular_value_patients.csv")

