import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and clean data
df = pd.read_csv("filtered_bills.csv")
df.columns = df.columns.str.strip()  # Remove extra spaces
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Step 2: Filter for age 0 patients
df_age_0 = df[df["Age"] == 1]

# Step 3: Extract only necessary columns
df_subset = df_age_0[["Consulted By", "Cadance Mapping", "Item"]].copy()

# Step 4: Manually enter the target doctors (use exact names from the CSV)
target_doctors = [
    "Dr Indu S Nair",
    "Dr. Bhaskar MV",
    "Dr. Shivangi Bora",
    "Dr. Vidisha",
    "Dr. Anamika Krishnan",
    "Dr Cajetan Tellis"
]

# Step 5: Count vaccines prescribed by each doctor
vaccine_counts = {}

for doctor in target_doctors:
    # Filter rows for this doctor
    doc_df = df_subset[df_subset["Consulted By"] == doctor]
    
    # Further filter rows where 'Item' contains 'vaccine'
    doc_vaccines = doc_df[doc_df["Cadance Mapping"].str.contains("Vaccine", case=False, na=False)]
    
    # Count total prescriptions (rows)
    vaccine_counts[doctor] = len(doc_vaccines)

# Step 6: Create bar chart
vaccine_series = pd.Series(vaccine_counts).sort_values()

plt.figure(figsize=(10, 6))
bars = plt.barh(vaccine_series.index, vaccine_series.values, color='darkorange')

# Add data labels
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2,
             str(int(width)), va='center', ha='left', fontsize=10)

plt.xlabel("Number of Vaccine Prescriptions")
plt.ylabel("Doctor")
plt.title("Vaccine Prescriptions by Doctor (Age 1 Patients)")
plt.tight_layout()
plt.savefig("vaccine_sales_by_doctor.png")
plt.show()

print("✅ Graph saved as 'vaccine_sales_by_doctor.png'")
