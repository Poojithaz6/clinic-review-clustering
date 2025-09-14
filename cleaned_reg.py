import pandas as pd

# Step 1: Load cleaned regular visits data
df = pd.read_csv("regular_visits.csv")

# Step 2: Standardize the Bill Date format
df['Bill Date'] = pd.to_datetime(df['Bill Date'], errors='coerce')

# Step 3: Remove any rows with invalid or missing dates
df = df.dropna(subset=['Bill Date'])

# Step 4: Normalize dates to a consistent format (YYYY-MM-DD)
df['Bill Date'] = df['Bill Date'].dt.normalize()

# Step 5: Group again to consolidate duplicate visits per patient per day
df_grouped = df.groupby(['Patient File No', 'Patient Name', 'Bill Date'])['Total Paid Amt'].sum().reset_index()

# Optional: Rename column
df_grouped = df_grouped.rename(columns={'Total Paid Amt': 'Total Spent'})

# Step 6: Save the final cleaned and grouped data
df_grouped.to_csv("regular_visits_final.csv", index=False)

print("✅ Final regular visits data saved to 'regular_visits_final.csv'. Dates normalized and amounts regrouped.")
