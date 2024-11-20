# Import libraries  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Load the dataset  
df = pd.read_csv("State_Data.csv")  
  
# Generate a heatmap  
plt.figure(figsize=(12, 8))  
sns.heatmap(df.set_index('State')[['Population (millions)', 'GDP (billions)', 'Personal Income (billions)']], annot=True, cmap='YlGnBu', linewidths=0.5)  
plt.title('Heatmap of Economic Parameters by State')  
plt.show()
