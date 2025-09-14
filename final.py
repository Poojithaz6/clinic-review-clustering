import pandas as pd

# Load cleaned demographics data
df = pd.read_csv("regular_visits_with_demographics.csv")

# Convert Bill Date to datetime
df['Bill Date'] = pd.to_datetime(df['Bill Date'], dayfirst=True, errors='coerce')

# Drop rows with missing essentials
df = df.dropna(subset=['Patient Name', 'Patient File No', 'Bill Date', 'Total Paid Amt'])

# Ensure amount is numeric
df['Total Paid Amt'] = pd.to_numeric(df['Total Paid Amt'], errors='coerce').fillna(0)

# Identify each visit: unique patient + unique date
unique_visits = df.groupby(['Patient File No', 'Patient Name', 'Bill Date'], as_index=False)['Total Paid Amt'].sum()

# Count visits and compute average spending per patient
visit_summary = unique_visits.groupby(['Patient File No', 'Patient Name']).agg(
    Total_Visits=('Bill Date', 'count'),
    Avg_Spent=('Total Paid Amt', 'mean')
).reset_index()

# Merge visit summary back into the original demographics data
df = pd.merge(df, visit_summary, on=['Patient File No', 'Patient Name'], how='left')

# Save updated data
df.to_csv("regular_visits_with_demographics.csv", index=False)

print("✅ 'Total_Visits' and 'Avg_Spent' columns added to demographics_data.csv.")
