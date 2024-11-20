# Import libraries  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Load the dataset  
df = pd.read_csv("State_Data.csv")  

# Define the columns to plot
columns = ['Population (millions)', 'GDP (billions)', 'Personal Income (billions)']

# Create a grid for the heatmaps
fig, axes = plt.subplots(1, 3, figsize=(20, 10), constrained_layout=True)

for ax, col in zip(axes, columns):
    sns.heatmap(df.set_index('State')[[col]], annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5, ax=ax)
    ax.set_title(f'Heatmap of {col}')

plt.suptitle('Heatmaps of Economic Parameters by State')
plt.show()
