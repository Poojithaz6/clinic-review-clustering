import pandas as pd

# Load the demographics data
df = pd.read_csv('regular_visits_with_demographics.csv')

# Convert Bill Date to datetime
df['Bill Date'] = pd.to_datetime(df['Bill Date'], dayfirst=True, errors='coerce')

# Drop any rows where critical data is missing
df = df.dropna(subset=['Patient Name', 'Bill Date', 'Total Paid Amt'])

# Convert amount column to numeric
df['Total Paid Amt'] = pd.to_numeric(df['Total Paid Amt'], errors='coerce').fillna(0)

# Group by Patient Name and Bill Date and sum up the amount
df_grouped = df.groupby(['Patient Name', 'Bill Date'], as_index=False)['Total Paid Amt'].sum()

# Save back to the same file
df_grouped.to_csv('regular_visits_with_demographics.csv', index=False)

print("✅ Combined and saved: multiple bills per patient per date are now merged into one row.")

