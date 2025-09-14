import pandas as pd

# Load the two datasets
clinic_df = pd.read_csv("clinic_data.csv")
regular_df = pd.read_csv("regular_visits.csv")

# Select relevant columns and drop duplicates to avoid messy join
demographics_df = clinic_df[['Patient File No', 'Patient Name', 'Age', 'Sex']].drop_duplicates()

# Merge on both Patient File No and Name
merged_df = pd.merge(regular_df, demographics_df, on=['Patient File No', 'Patient Name'], how='left')

# Save the updated regular visits data
merged_df.to_csv("regular_visits_with_demographics.csv", index=False)

print("✅ Demographics added and saved as 'regular_visits_with_demographics.csv'")
