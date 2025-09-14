import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load cleaned demographic data
df = pd.read_csv("regular_visits_with_demographics.csv")

# Step 2: Drop rows with missing Age or Avg_Spent
df = df.dropna(subset=['Age', 'Avg_Spent'])

# Step 3: Feature selection
X = df[['Age', 'Avg_Spent']]

# Step 4: KMeans Clustering (try 3 clusters first)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)

# Step 5: Save clustered data
df.to_csv("clustered_patients.csv", index=False)

# Step 6: Cluster Centers
centers = pd.DataFrame(kmeans.cluster_centers_, columns=['Age', 'Avg_Spent'])
print("\n📍 Cluster Centers:")
print(centers)

# Step 7: Human-readable Insights
print("\n📊 Cluster Spending Insights:")
for i, row in centers.iterrows():
    print(f"Cluster {i}: Avg Age = {row['Age']:.1f}, Avg Spend = ₹{row['Avg_Spent']:.2f}")

# Step 8: Visualize Scatter Plot
plt.figure(figsize=(8, 6))
for cluster in df['Cluster'].unique():
    plt.scatter(
        df[df['Cluster'] == cluster]['Age'],
        df[df['Cluster'] == cluster]['Avg_Spent'],
        label=f'Cluster {cluster}'
    )

# Mark the centroids
plt.scatter(centers['Age'], centers['Avg_Spent'], color='black', marker='X', s=200, label='Centroids')

plt.xlabel("Age")
plt.ylabel("Avg Spending (₹)")
plt.title("KMeans Clustering of Pediatric Patients")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("patient_clusters.png")
# plt.show()  # Skip for terminal usage

# Step 9: Bar chart of avg spending per cluster
avg_per_cluster = df.groupby('Cluster')['Avg_Spent'].mean().sort_values(ascending=False)

plt.figure(figsize=(7, 5))
avg_per_cluster.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Average Spending by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Avg Spending (₹)")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("spending_by_cluster.png")
# plt.show()  # Again, skip for headless Linux

print("\n📁 Clustered CSV saved as: clustered_patients.csv")
print("📊 Charts saved as: patient_clusters.png and spending_by_cluster.png")
