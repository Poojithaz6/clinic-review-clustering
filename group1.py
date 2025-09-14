import pandas as pd

# Load the data
df = pd.read_csv("regular_visits_with_demographics.csv")

# Convert Bill Date to datetime
df['Bill Date'] = pd.to_datetime(df['Bill Date'], dayfirst=True, errors='coerce')

# Drop rows with essential missing info
df = df.dropna(subset=['Patient Name', 'Bill Date', 'Total Paid Amt'])

# Ensure amount column is numeric
df['Total Paid Amt'] = pd.to_numeric(df['Total Paid Amt'], errors='coerce').fillna(0)

# Group and aggregate
df_grouped = df.groupby(['Patient Name', 'Bill Date'], as_index=False).agg({
    'Total Paid Amt': 'sum',
    'Age': 'first',
    'Sex': 'first',
    'Bill No': 'first',
    'Patient File No': 'first',  # add more columns as needed
})

# Save the cleaned and grouped data back
df_grouped.to_csv("regular_visits_with_demographics.csv", index=False)

print("✅ Grouped and saved with Age, Sex, Bill No retained.")
