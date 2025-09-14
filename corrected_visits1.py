import pandas as pd

# Load dataset
df = pd.read_csv("clinic_data.csv")

# Convert Bill Date to datetime
df['Bill Date'] = pd.to_datetime(df['Bill Date'], errors='coerce')

# Drop rows with missing critical info
df = df.dropna(subset=['Patient File No', 'Patient Name', 'Bill Date', 'Paid Amt'])

# Group by patient and date (each date = 1 visit)
visit_df = df.groupby(['Patient File No', 'Patient Name', 'Bill Date'])['Paid Amt'].sum().reset_index()
visit_df = visit_df.rename(columns={'Paid Amt': 'Total Paid Amt'})

# ❌ Remove visits where total is 0
visit_df = visit_df[visit_df['Total Paid Amt'] > 0]

# Split high and regular spenders
high_value_visits = visit_df[visit_df['Total Paid Amt'] > 11000]
regular_visits = visit_df[visit_df['Total Paid Amt'] <= 11000]

# Save both
high_value_visits.to_csv("high_value_visits.csv", index=False)
regular_visits.to_csv("regular_visits.csv", index=False)

print("✅ Cleaning done. Files saved.")
