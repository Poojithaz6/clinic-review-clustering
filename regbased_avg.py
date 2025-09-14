import pandas as pd

# Load full billing data
df = pd.read_csv("regular_value_patients.csv", na_values=["", " ", "NA", "N/A", "None", "-"])

# Clean + parse dates
df['Bill Date'] = pd.to_datetime(df['Bill Date'], errors='coerce')
df = df.dropna(subset=['Patient File No', 'Patient Name', 'Bill Date', 'Paid Amt'])

# Group by patient and bill date to get total per visit
per_visit_df = df.groupby(['Patient File No', 'Patient Name', 'Bill Date'])['Paid Amt'].sum().reset_index()

# Load regular patients
regular_df = pd.read_csv("regular_value_patients.csv")

# Keep only regular patients' visits
regular_visits = pd.merge(
    per_visit_df,
    regular_df[['Patient File No', 'Patient Name']],
    on=['Patient File No', 'Patient Name'],
    how='inner'
)

# Now group again by patient to get:
# - total paid
# - number of unique visit days
summary_df = regular_visits.groupby(['Patient File No', 'Patient Name']).agg(
    total_paid=('Paid Amt', 'sum'),
    unique_visit_days=('Bill Date', 'nunique')
).reset_index()

# Final avg per patient (based on real visit days)
summary_df['avg_paid_per_unique_visit'] = summary_df['total_paid'] / summary_df['unique_visit_days']

# Save to CSV
summary_df.to_csv("regular_patient_per_unique_visit_avg.csv", index=False)

print("✅ Cumulative avg per regular patient (by visit day) calculated.")
print("📁 Saved as: regular_patient_per_unique_visit_avg.csv")

