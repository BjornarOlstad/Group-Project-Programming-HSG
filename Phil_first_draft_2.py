# Import Libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset  
df = pd.read_csv("State_Data.csv")  

# Prepare date for clustering  
X = df[['Population (millions)', 'GDP (billions)', 'Personal Income (billions)',   
        'Subsidies (millions)', 'Comp of Emp (billions)', 'Tax on Prod/Imp (billions)']]  
  
# Standardize data  
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
X_scaled = scaler.fit_transform(X)  
  
# KMeans clustering  
kmeans = KMeans(n_clusters=4, random_state=51)  
clusters = kmeans.fit_predict(X_scaled)  
  
# Add cluster labels to the dataframe

df['Cluster'] = clusters  
  
# Visualize the clusters  
plt.figure(figsize=(12, 8))  
sns.scatterplot(x='GDP (billions)', y='Personal Income (billions)', hue='Cluster', data=df, palette='viridis')  
plt.title("Cluster Analysis of States based on Economic Indicators")  
plt.xlabel("GDP (billions)")  
plt.ylabel("Personal Income (billions)")  
plt.legend(title='Cluster')  
plt.show()
