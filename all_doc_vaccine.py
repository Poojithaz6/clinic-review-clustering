import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and clean data
df = pd.read_csv("filtered_bills - filtered_bills (1).csv")
df.columns = df.columns.str.strip()
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Step 2: Filter age 0 only
df_age0 = df[df["Age"] == 2].copy()

# Step 3: Define visit key (same patient, same doctor, same date = one visit)
df_age0["VisitID"] = (
    df_age0["Patient File No"].astype(str) + "_" +
    df_age0["Consulted By"].astype(str) + "_" +
    df_age0["Bill Date"].astype(str)
)

# Step 4: Determine which visits involved a vaccine
# Find VisitIDs that contain a vaccine item
df_age0["is_vaccine"] = df_age0["Cadance Mapping"].str.contains("Vaccine", case=False, na=False)
vaccine_visits = set(df_age0[df_age0["is_vaccine"]]["VisitID"])

# Step 5: Aggregate visit data and mark vaccinated status
# Keep only first row per visit (after grouping)
df_visits = df_age0.drop_duplicates(subset=["VisitID"]).copy()
df_visits["Vaccinated"] = df_visits["VisitID"].apply(lambda x: "Yes" if x in vaccine_visits else "No")

# Step 6: Select final columns
final_columns = [
    "Patient Name", "Sex", "Age", "Consulted By", "Bill Date", "Vaccinated"
]
df_final = df_visits[final_columns]

# Step 7: Save the updated visit-level data
df_final.to_csv("age1_visits_with_vaccination_status.csv", index=False)
print("✅ CSV saved as 'age1_visits_with_vaccination_status.csv'")
# Step 8: Plot vaccinated vs not vaccinated per doctor
summary = df_final.groupby(["Consulted By", "Vaccinated"]).size().unstack(fill_value=0)

# Plot
plt.figure(figsize=(12, 6))
summary.plot(kind='bar', stacked=False, color=["tomato", "mediumseagreen"])

plt.xlabel("Doctor")
plt.ylabel("Number of Visits")
plt.title("Vaccinated vs Not Vaccinated Visits (Patients Aged 2)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("vaccinated_vs_not_vaccinated_fixed_per_doctor.png")
plt.show()

print("✅ Graph saved as 'vaccinated_vs_not_vaccinated_fixed_per_doctor1.png'")
