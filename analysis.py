import matplotlib.pyplot as plt

# Group 1: Age Group Spending Chart
age_bins = [0, 2, 5, 8, 12]
age_labels = ['0–2 (Infants)', '3–5 (Toddlers)', '6–8 (Early School Age)', '9–12 (Pre-teens)']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=True, include_lowest=True)
age_group_summary = df.groupby('Age Group')['Avg_Spent'].mean().sort_values(ascending=False)

# Plot 1: Average Spending by Age Group
plt.figure(figsize=(10, 6))
age_group_summary.sort_index().plot(kind='bar', color='salmon', edgecolor='black')
plt.title("Average Spending by Pediatric Age Group", fontsize=14)
plt.xlabel("Age Group")
plt.ylabel("Average Amount Spent (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("spending_by_age_group.png")
plt.show()

# Group 2: Sex Spending Chart
sex_spending = df.groupby('Sex')['Avg_Spent'].mean().sort_values(ascending=False)

# Plot 2: Average Spending by Sex
plt.figure(figsize=(8, 5))
sex_spending.plot(kind='bar', color='mediumseagreen', edgecolor='black')
plt.title("Average Spending by Sex", fontsize=14)
plt.xlabel("Sex")
plt.ylabel("Average Amount Spent (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("spending_by_sex.png")
plt.show()
