# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset containing economic indicators of states
df = pd.read_csv("State_Data.csv")

# Select relevant columns for clustering
X = df[['Population (millions)', 'GDP (billions)', 'Personal Income (billions)',
        'Subsidies (millions)', 'Comp of Emp (billions)', 'Tax on Prod/Imp (billions)']]

# Standardize the data to ensure all features are on the same scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform KMeans clustering with four clusters
# Four clusters are chosen to group states into distinct economic categories.
kmeans = KMeans(n_clusters=4, random_state=51)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original DataFrame
df['Cluster'] = clusters

# Sort clusters by mean GDP and reassign cluster numbers
cluster_order = df.groupby('Cluster')['GDP (billions)'].mean().sort_values().index
cluster_mapping = {old: new for new, old in enumerate(cluster_order)}
df['Cluster'] = df['Cluster'].map(cluster_mapping)

# Count of states in each cluster
# Used to annotate the legend in the scatterplot
cluster_counts = df['Cluster'].value_counts().sort_index()

# Create a scatterplot to visualize clusters with state counts in the legend
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(x='GDP (billions)', y='Personal Income (billions)', hue='Cluster', data=df, palette='viridis')
handles, labels = scatter.get_legend_handles_labels()
labels = [f"Cluster {i} ({cluster_counts[i]} states)" for i in range(len(cluster_counts))]
plt.legend(handles=handles, labels=labels, title="Cluster")
plt.title("Cluster Analysis of States (Ordered by GDP)")
plt.xlabel("GDP (billions)")
plt.ylabel("Personal Income (billions)")
plt.show()

# Define a list of variables to generate boxplots for
variables = ['GDP (billions)', 'Personal Income (billions)', 
             'Population (millions)', 'Comp of Emp (billions)']

# Generate boxplots for the selected variables in a grid layout
plt.figure(figsize=(16, 12))  # Adjust the figure size to fit all plots
for i, var in enumerate(variables):
    plt.subplot(2, 2, i + 1) 
    sns.boxplot(x='Cluster', y=var, data=df, palette='viridis')
    plt.title(f"{var} Distribution Across Clusters")
    plt.xlabel("Cluster")
    plt.ylabel(var)
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show(
