import pandas as pd

# Load the cleaned regular patient data
df = pd.read_csv("regular_value_patients.csv")

# Ensure Bill Date is in datetime format
df['Bill Date'] = pd.to_datetime(df['Bill Date'], errors='coerce')
df = df.dropna(subset=['Patient File No', 'Patient Name', 'Bill Date', 'Paid Amt'])

# Group by patient and bill date to get visit-level spend
visit_level = df.groupby(['Patient File No', 'Patient Name', 'Bill Date'])['Paid Amt'].sum().reset_index()

# Now group by patient to get total paid and unique visit count
summary_df = visit_level.groupby(['Patient File No', 'Patient Name']).agg(
    total_paid=('Paid Amt', 'sum'),
    unique_visit_days=('Bill Date', 'nunique')
).reset_index()

# Final average
summary_df['avg_paid_per_unique_visit'] = summary_df['total_paid'] / summary_df['unique_visit_days']

# Save to file
summary_df.to_csv("regular_patient_unique_visit_avg.csv", index=False)

print("✅ Avg paid per unique visit (from cleaned DB) saved.")
print("📁 File: regular_patient_unique_visit_avg.csv")
