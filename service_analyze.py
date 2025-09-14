import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("filtered_bills.csv")

# Clean column names (remove any spaces)
df.columns = df.columns.str.strip()

# Check the actual column names
print("Columns in file:", df.columns.tolist())

# Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Filter patients aged 0
df_age_0 = df[df["Age"] == 0]
print("Number of records with age 0:", len(df_age_0))

# Check if essential columns exist
if "ServiceCategory" not in df_age_0.columns or "Patient Unique ID" not in df_age_0.columns:
    print("Required columns missing: 'ServiceCategory' or 'Patient Unique ID'")
else:
    # Group and count unique patients by service
    service_usage = df_age_0.groupby("ServiceCategory")["Patient Unique ID"].nunique().sort_values()

    print("Service usage counts:\n", service_usage)

    # Plot only if there is data
    if not service_usage.empty:
        plt.figure(figsize=(10, 6))
        service_usage.plot(kind='barh', color='lightgreen')
        plt.xlabel("Number of Patients (Age 0)")
        plt.ylabel("Service Category")
        plt.title("Services Used by Patients Aged 0")
        plt.tight_layout()
        plt.savefig("services_by_age_0.png")
        print("Graph saved as 'services_by_age_0.png'")
    else:
        print("No data to plot.")

