import pandas as pd

# Load and clean data
df = pd.read_csv("filtered_bills.csv")
df.columns = df.columns.str.strip()
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Step 1: Filter only age 0 patients
df_age0 = df[df["Age"] == 0].copy()

# Step 2: Create a column 'Vaccinated' default = "No"
df_age0["Vaccinated"] = "No"

# Step 3: Identify vaccine events (Item contains 'vaccine')
df_vax = df_age0[df_age0["Cadance Mapping"].str.contains("Vaccine", case=False, na=False)]

# Step 4: Create a key to identify each visit
df_age0["visit_id"] = df_age0["Patient File No"].astype(str) + "_" + df_age0["Bill No"].astype(str) + "_" + df_age0["Bill Date"].astype(str)
df_vax["visit_id"] = df_vax["Patient File No"].astype(str) + "_" + df_vax["Bill No"].astype(str) + "_" + df_vax["Bill Date"].astype(str)

# Step 5: Mark visits that included vaccines
vaccinated_visits = set(df_vax["visit_id"])
df_age0["Vaccinated"] = df_age0["visit_id"].apply(lambda x: "Yes" if x in vaccinated_visits else "No")

# Step 6: Drop duplicate visits (we only want one row per visit)
df_visits = df_age0.drop_duplicates(subset=["visit_id"])

# Step 7: Select key columns
final_columns = [
    "Patient Name", "Sex", "Age", "Consulted By",
    "Bill No", "Bill Date", "Vaccinated"
]
other_cols = [col for col in df_visits.columns if col not in final_columns]
df_final = df_visits[final_columns + other_cols]

# Save to CSV
df_final.to_csv("age0_all_visits_with_vaccine_status.csv", index=False)
print("✅ CSV saved as 'age0_all_visits_with_vaccine_status.csv'")
