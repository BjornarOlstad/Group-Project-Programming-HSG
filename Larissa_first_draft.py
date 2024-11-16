#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("State_Data.csv")

# Create list of available columns for comparison
columns = [
    'Population (millions)', 'GDP (billions)', 'Personal Income (billions)',
    'Subsidies (millions)', 'Comp of Emp (billions)', 'Tax on Prod/Imp (billions)'
]

# Function to prompt the user to select a column
def select_column(prompt):
    #print the instruction for the user 
    print(prompt)
    # Loop through the columns and display them with corresponding numbers starting from 1
    for i, column in enumerate(columns, 1):
        print(f"{i}. {column}")
    # Loop until the user enters a valid choice
    while True:
        try:
            # Prompt the user to enter a number corresponding to the column
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(columns):
                # If the user enters a valid choice, return the selected column
                # Add a new line for better readability
                print("\n")
                return columns[choice - 1]
            else:
                # If the user enters a number that is not in the valid range, display an error message
                print("Invalid choice. Please enter a number between 1 and", len(columns))
        except ValueError:
            #If the user enters a non-integer value, display an error message
            print("Invalid input. Please enter a number.")

# Prompt the user to select the first and second columns for comparison
column1 = select_column("Select the first parameter to compare:")
column2 = select_column("Select the second parameter to compare:")
# Loop to ensure that the second column is different from the first column
while column1 == column2:
    column2 = select_column("Invalid choice. Please select a different parameter to compare:")

# Extract the data for the selected columns
data1 = df[column1]
data2 = df[column2]

# Calculate the correlation
correlation = data1.corr(data2)

# Print the correlation
print(f"Correlation between {column1} and {column2}: {correlation}")

# Create a scatter plot
plt.figure(figsize=(10, 6))

# Add a super title for the entire figure
plt.suptitle('Correlation Analysis', fontsize=16)

# Create a scatter plot of the two selected columns
#Set alpha to 0.5 to make the points semi-transparent for better visualisation of overlapping points
plt.scatter(data1, data2, alpha=0.5)
# Set a title, using 'column1' and 'column2' to make the title specific to the chosen columns
plt.title(f'{column1} vs. {column2}')
#Label the x and y axis
plt.xlabel(column1)
plt.ylabel(column2)

#Display scatter plot
plt.show()