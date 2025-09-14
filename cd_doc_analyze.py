import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("filtered_bills - filtered_bills (1).csv")
df.columns = df.columns.str.strip()  # Clean column names
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Filter for patients aged 0
df_age_0 = df[df["Age"] == 1]
# ---------- GRAPH 2: Preferred Doctor ----------
# Clean and drop missing doctor names
df_age_0["Consulted By"] = df_age_0["Consulted By"].replace(r"^\s*$", pd.NA, regex=True)
df_doctors = df_age_0.dropna(subset=["Consulted By"])
doctor_usage = df_doctors["Consulted By"].value_counts().sort_values()

# Plot Preferred Doctors
plt.figure(figsize=(10, 6))
bars = plt.barh(doctor_usage.index, doctor_usage.values, color='lightgreen')
plt.xlabel("Number of Patients")
plt.ylabel("Consulted By (Doctor)")
plt.title("Preferred Doctors for Patients Aged 1")
for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, str(int(bar.get_width())), va='center')
plt.tight_layout()
plt.savefig("doctors_by_age_1.png")
print("✅ Graph 2 saved: 'doctors_by_age_1.png'")
