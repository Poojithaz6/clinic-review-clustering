# analyze_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv("regular_visits_with_demographics.csv")

# Create label: high spender if Avg_Spent > 4000
df['HighSpender'] = (df['Avg_Spent'] > 4000).astype(int)

# Select features
features = ['Age', 'Total_Visits']
df = df.dropna(subset=features + ['HighSpender'])  # remove rows with missing values
X = df[features]
y = df['HighSpender']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
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
