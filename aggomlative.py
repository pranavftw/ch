# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 1: Load dataset (Using Iris dataset as an example)
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) as a column
iris_df['species'] = iris.target
iris_df.to_csv('iris_dataset.csv', index=False)


#X hold the sepal and petal length & width
X = iris.data
# y is 1d array which hold 0 → Iris setosa
# 1 → Iris versicolor
# 2 → Iris virginica

y = iris.target

# Step 2: Preprocessing (optional scaling)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply Agglomerative Clustering
# Create the model
agglo_clustering = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

# Fit the model
clusters = agglo_clustering.fit_predict(X_scaled)
# Step 4: store the predicted clusters for each row in csv file
predicted_clusters_df = pd.DataFrame({
    'Sample Index': np.arange(len(clusters)),  # Index of each sample
    'Predicted Cluster': clusters                # Predicted cluster labels
})

# Step 5: Save the DataFrame to a CSV file
predicted_clusters_df.to_csv('predicted_clusters.csv', index=False)



# Step 4: Visualize the clustering results with Dendrogram
# Perform linkage for dendrogram (for hierarchical clustering visualization)
linked = linkage(X_scaled, method='single')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=iris.target_names[y],
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Dendrogram for Agglomerative Hierarchical Clustering')
plt.xlabel('Samples')
plt.ylabel('Euclidean Distance')
plt.savefig('dendrogram.png')

# Step 5: Analyze Clustering Result
# Scatter plot of the clusters in 2D
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='rainbow')
plt.title('Agglomerative Clustering Results (3 Clusters)')
plt.xlabel('Feature 1 (scaled)')
plt.ylabel('Feature 2 (scaled)')
plt.savefig('agglomerative.png')