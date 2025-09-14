import pandas as pd

# Load the dataset
df = pd.read_csv("clinic_data.csv", na_values=["", " ", "NA", "N/A", "None", "-"])

# Drop rows with missing patient identifiers
df = df.dropna(subset=['Patient File No', 'Patient Name'])

# Drop duplicates to get unique patients
unique_patients = df[['Patient File No', 'Patient Name']].drop_duplicates()

# Count of unique patients
num_unique_patients = unique_patients.shape[0]

print(f"✅ Number of unique patients: {num_unique_patients}\n")
print("🧾 List of unique patients:")
print(unique_patients)

# Optional: Save to CSV
unique_patients.to_csv("unique_patients.csv", index=False)
print("\n📁 Saved as: unique_patients.csv")
