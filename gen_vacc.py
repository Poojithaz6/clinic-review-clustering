import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("filtered_bills.csv")
df.columns = df.columns.str.strip()

# Manually define the target doctors (use exact names from your CSV)
target_doctors = [
   "Dr Indu S Nair",
    "Dr. Bhaskar MV",
    "Dr. Shivangi Bora",
    "Dr. Vidisha",
    "Dr. Anamika Krishnan",
    "Dr Cajetan Tellis"
]

# Filter only for rows where 'Item' contains 'vaccine' (case-insensitive)
vaccine_rows = df[df["Cadance Mapping"].str.contains("Vaccine", case=False, na=False)]

# Filter only the selected doctors
vaccine_rows = vaccine_rows[vaccine_rows["Consulted By"].isin(target_doctors)]

# Count number of vaccine prescriptions per doctor (not unique)
vaccine_counts = vaccine_rows["Consulted By"].value_counts().reindex(target_doctors, fill_value=0)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.barh(vaccine_counts.index, vaccine_counts.values, color="seagreen")

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2,
             str(int(width)), va='center', ha='left', fontsize=10)

# Labeling
plt.xlabel("Number of Vaccine Prescriptions")
plt.ylabel("Doctor")
plt.title("Vaccine Prescriptions by Doctor (All Ages)")
plt.tight_layout()
plt.savefig("vaccine_prescriptions_by_doctor_all_ages.png")
plt.show()

print("✅ Graph saved as 'vaccine_prescriptions_by_doctor_all_ages.png'")
