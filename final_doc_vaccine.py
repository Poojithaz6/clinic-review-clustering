import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load and clean data
df = pd.read_csv("filtered_bills - filtered_bills (1).csv")
df.columns = df.columns.str.strip()
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Step 2: Filter for age 0
df_age0 = df[df["Age"] == 2].copy()

# Step 3: Filter only target doctors
target_doctors = [
    "Dr. Shivangi Bora",
    "Dr. Anamika Krishnan",
    "Dr. Vidisha",
    "Dr. Bhaskar MV",
    "Dr K Swapna",
    "Dr Indu S Nair"
]

df_age0 = df_age0[df_age0["Consulted By"].isin(target_doctors)]

# Step 4: Define visit ID as (Patient, Doctor, Date)
df_age0["VisitID"] = (
    df_age0["Patient File No"].astype(str) + "_" +
    df_age0["Consulted By"].astype(str) + "_" +
    df_age0["Bill Date"].astype(str)
)

# Step 5: Flag if a vaccine was prescribed in that row
df_age0["is_vaccine"] = df_age0["Cadance Mapping"].str.contains("Vaccine", case=False, na=False)
vaccine_visits = set(df_age0[df_age0["is_vaccine"]]["VisitID"])

# Step 6: Mark each visit as Vaccinated = Yes/No
df_visits = df_age0.drop_duplicates(subset=["VisitID"]).copy()
df_visits["Vaccinated"] = df_visits["VisitID"].apply(lambda x: "Yes" if x in vaccine_visits else "No")

# Step 7: Select final columns
final_columns = [
    "Patient Name", "Sex", "Age", "Consulted By", "Bill Date", "Vaccinated"
]
df_final = df_visits[final_columns]

# Step 8: Save to CSV in 'ml_project' folder
os.makedirs("ml_project", exist_ok=True)
df_final.to_csv("ml_project/age0_visits_with_vaccination_status.csv", index=False)
print("✅ CSV saved at 'ml_project/age0_visits_with_vaccination_status.csv'")

# Step 9: Create grouped bar chart per doctor
summary = df_final.groupby(["Consulted By", "Vaccinated"]).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
summary.plot(kind='bar', stacked=False, color=["tomato", "mediumseagreen"])

plt.xlabel("Doctor")
plt.ylabel("Number of Visits")
plt.title("Vaccinated vs Not Vaccinated Visits per Doctor (Age 2)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save plot
plt.savefig("ml_project/vaccinated_vs_not_vaccinated_per_doctor.png")
plt.show()
print("✅ Graph saved as 'ml_project/vaccinated_vs_not_vaccinated_per_doctor.png'")
