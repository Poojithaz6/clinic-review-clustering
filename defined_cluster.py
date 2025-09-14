import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and clean data
df = pd.read_csv("regular_visits_with_demographics.csv")
df = df.dropna(subset=['Age', 'Avg_Spent'])

# Step 2: Create Supervised Age Groups (manually defined)
bins = [0, 4, 8, 12]
labels = [1, 2, 3]  # Cluster labels you defined
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True, include_lowest=True)

# Step 3: Save labeled data
df.to_csv("supervised_age_groups.csv", index=False)

# Step 4: Calculate and print average spending per group
summary = df.groupby('Age_Group')['Avg_Spent'].mean()
print("\n📊 Average Spend by Supervised Age Group:")
for group, avg in summary.items():
    age_desc = {
        1: "0–4 (Infants/Toddlers)",
        2: "5–8 (School Age)",
        3: "9–12 (Pre-teens)"
    }[int(group)]
    print(f"Group {group} ({age_desc}): ₹{avg:.2f}")

# Step 5: Bar Chart
plt.figure(figsize=(8, 5))
summary.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Avg Spending per Supervised Age Group")
plt.xlabel("Age Group (Cluster ID)")
plt.ylabel("Avg Spending (₹)")
plt.xticks(ticks=[0, 1, 2], labels=["0–4", "5–8", "9–12"], rotation=0)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("supervised_age_group_spending.png")
# plt.show() ← use this if running in notebook
