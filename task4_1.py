def task1():
    """
    Task 1: Data Analysis and Visualization.
    This task allows the user to select a region and a state to analyze data,
    and provides visualizations such as bar and pie charts.
    """
    
    print("Task 1: Data Analysis and Visualization")

# Importing required libraries
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Reading the dataset into a DataFrame
df = pd.read_csv("State_Data.csv")  

# Selecting the specific columns to visualize
columns = ['Population (millions)', 'GDP (billions)', 'Personal Income (billions)']

# Initializing a subplot grid for displaying multiple heatmaps
fig, axes = plt.subplots(1, 3, figsize=(22, 16), constrained_layout=True)

# Looping through the axes and corresponding columns to generate sorted heatmaps
for ax, col in zip(axes, columns):
    # Sorting the DataFrame by the current column in descending order
    # The 'State' column remains intact as it is not reset or dropped
    sorted_df = df.sort_values(by=col, ascending=False)
    
    # Creating a heatmap for the sorted data
    sns.heatmap(sorted_df.set_index('State')[[col]], annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5, ax=ax)
    
    # Adding a title above each subplot to specify the represented parameter
    ax.set_title(f'Heatmap of {col} (sorted)')

# Defining a central title for the entire plot
plt.suptitle('Sorted Heatmaps of Economic Parameters by State', fontsize=16)

# Rendering the figure to display the visualizations
plt.show()
