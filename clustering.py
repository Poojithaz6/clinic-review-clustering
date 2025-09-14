import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the cleaned file
df = pd.read_csv("regular_visits_with_demographics.csv")

# Step 2: Drop nulls (if any)
df = df.dropna(subset=['Avg_Spent', 'Age'])

# Step 3: Feature Selection
X = df[['Age', 'Avg_Spent']]

# Step 4: KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Step 5: Cluster Centers and Labeling
centers = kmeans.cluster_centers_
print("\n📍 Cluster Centers (Age, Avg_Spent):\n", centers)

# Step 6: Save clustered data
df.to_csv("clustered_patients.csv", index=False)

# Step 7: Visualization
plt.figure(figsize=(8, 6))
for cluster in df['Cluster'].unique():
    clustered = df[df['Cluster'] == cluster]
    plt.scatter(clustered['Age'], clustered['Avg_Spent'], label=f'Cluster {cluster}')
    
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='X', s=200, label='Centroids')
plt.xlabel("Age")
plt.ylabel("Avg Spending (₹)")
plt.title("KMeans Clustering of Patients")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("patient_clusters.png")
# plt.show()  # Use only if running with GUI
