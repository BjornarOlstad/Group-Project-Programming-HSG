from sklearn.cluster import KMeans  
import seaborn as sns  
  
# Prepare the data for clustering  
X = df[['Population (millions)', 'GDP (billions)', 'Personal Income (billions)',   
        'Subsidies (millions)', 'Comp of Emp (billions)', 'Tax on Prod/Imp (billions)']]  
  
# Standardize the data  
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
X_scaled = scaler.fit_transform(X)  
  
# Apply KMeans clustering  
kmeans = KMeans(n_clusters=4, random_state=42)  
clusters = kmeans.fit_predict(X_scaled)  
  
# Add cluster labels to the dataframe  
df['Cluster'] = clusters  
  
# Visualize the clusters  
plt.figure(figsize=(10, 6))  
sns.scatterplot(x='GDP (billions)', y='Personal Income (billions)', hue='Cluster', data=df, palette='viridis')  
plt.title("Cluster Analysis of States based on Economic Indicators")  
plt.xlabel("GDP (billions)")  
plt.ylabel("Personal Income (billions)")  
plt.legend(title='Cluster')  
plt.show()
