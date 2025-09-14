import pandas as pd

# Load the original CSV file
df = pd.read_csv("clinic_data.csv")  # Replace with your actual file name

# Filter rows where Bill Amt < 11000
filtered_df = df[df["Total Amt"] < 11000]

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_bills.csv", index=False)

# Optional: print the filtered data
print(filtered_df)
