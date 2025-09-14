import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load cleaned dataset
df = pd.read_csv("regular_visits_with_demographics.csv")

# Step 2: Clean missing values
df = df.dropna(subset=['Age', 'Avg_Spent'])

# Step 3: Group by individual age
age_stats = df.groupby('Age').agg(
    Patient_Count=('Patient File No', 'nunique'),  # or use 'Patient Name'
    Avg_Spent=('Avg_Spent', 'mean')
).reset_index()

# Step 4: Only keep ages between 0 and 12
age_stats = age_stats[age_stats['Age'].between(0, 12)]

# Step 5: Plot bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(age_stats['Age'], age_stats['Patient_Count'], color='mediumslateblue', edgecolor='black')

# Add avg spend inside each bar
for bar, avg_spent in zip(bars, age_stats['Avg_Spent']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height/2, f"₹{avg_spent:.0f}",
             ha='center', va='center', fontsize=11, color='white', fontweight='bold')

plt.title("Number of Patients by Age with Avg Spending Shown", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.xticks(range(0, 13))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("patients_by_individual_age.png")
# plt.show()  # Optional if running with GUI
