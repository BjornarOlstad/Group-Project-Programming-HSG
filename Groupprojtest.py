# Summary:
# - data_list: Holds all state data.
# - state_data: Represents one state's data within loops.
# - result and region_data: Filtered lists for the selected region.
# - valid_regions and valid_states: Sets of unique region and state names.
# - selected_state_data: Detailed data for the user-selected state.

# Import libraries
import pandas as pd
# pip install matplotlib # Install in terminal if not already done 
import matplotlib.pyplot as plt

# Load the dataset and create a DataFrame from CSV file
df = pd.read_csv("State_Data.csv")

# Function to convert the DataFrame into a list of lists
# Purpose: To convert the dataset from a DataFrame to a structured list for easier filtering and manipulation
def load_data_as_list(df):
    # Initialize an empty list to store data for all states
    data_list = []
    
    # Loop over each row in the DataFrame
    for _, row in df.iterrows():
        # Create a list for each state with selected columns and convert values to actual numbers
        state_data = [
            row['State'],                            # State name
            row['Region'],                           # Region
            row['Population (millions)'] * 1_000_000,  # Population in actual numbers
            row['GDP (billions)'] * 1_000_000_000,     # GDP in actual dollars
            row['Personal Income (billions)'] * 1_000_000_000  # Personal income in dollars
        ]
        # Append the state_data list to data_list
        data_list.append(state_data)
    
    # Return the populated data_list with all states' data
    return data_list


# Function to filter states by region and calculate per capita values
# Purpose: To create a filtered list of states within the selected region and calculate per capita values for GDP and income
def calculate_per_capita_list(data_list, region):
    # Initialize an empty list to store data for states in the selected region
    result = []

    # Loop through each state's data in data_list
    for state_data in data_list:
        # Unpack values for clarity
        state, state_region, population, gdp, income = state_data
        
        # Check if the state's region matches the selected region (ignoring case)
        if state_region.lower() == region.lower():
            # Calculate per capita GDP and income
            gdp_per_capita = gdp / population
            income_per_capita = income / population
            
            # Append state's data with calculated per capita values to result list
            result.append([
                state,                 # State name
                state_region,          # Region name
                population,            # Population
                gdp,                   # GDP
                income,                # Personal income
                gdp_per_capita,        # Calculated GDP per capita
                income_per_capita      # Calculated income per capita
            ])
    
    # Return the list for the selected region with per capita values
    return result


# Function to prompt the user to select a valid region from data_list
# Purpose: To interactively get a valid region from the user based on available data
def get_valid_region(data_list):
    # Extract unique regions from data_list by selecting the region in each state_data
    valid_regions = {state_data[1] for state_data in data_list}
    
    # Loop to continually prompt until a valid region is entered
    while True:
        # Display valid regions and prompt the user for a choice
        region = input(f"Enter a region from the following list: {', '.join(valid_regions)}\n").strip()
        
        # Check if the entered region is valid
        if region in valid_regions:
            # If valid, return the region
            return region
        else:
            # If invalid, inform the user and prompt again
            print("Invalid region name. Please try again.")


# Function to prompt the user to select a valid state from region_data
# Purpose: To prompt the user for a specific state within the chosen region, and validate the choice
def get_valid_state(region_data):
    # Extract state names from region_data (first element in each list)
    valid_states = {state_data[0] for state_data in region_data}
    
    # Loop to continually prompt until a valid state is entered
    while True:
        # Prompt user to select a state within the chosen region
        state = input(f"Enter a state from the following list: {', '.join(valid_states)}\n").strip()
        
        # Check if the entered state is valid
        if state in valid_states:
            # If valid, find and return the data for this state
            for state_data in region_data:
                if state_data[0] == state:
                    return state_data
        else:
            # If invalid, inform the user and prompt again
            print("Invalid state name. Please try again.")


# Main program execution
# Purpose: To guide the user through selecting a region and a state, and display detailed information for the selected state
# Step 1: Load data as a list of lists
data_list = load_data_as_list(df)  # Call load_data_as_list with the loaded DataFrame

# Step 2: Prompt the user to select a valid region
selected_region = get_valid_region(data_list)

# Step 3: Filter data and calculate per capita values for states in the selected region
region_data = calculate_per_capita_list(data_list, selected_region)

# Step 4: Prompt the user to select a valid state from the region and get its information
selected_state_data = get_valid_state(region_data)

# Print information about the selected state in a readable format
print("\nInformation for the selected state:")
print(f"State: {selected_state_data[0]}")
print(f"Region: {selected_state_data[1]}")
print(f"Population: {selected_state_data[2]}")
print(f"GDP: {selected_state_data[3]}")
print(f"Personal Income: {selected_state_data[4]}")
print(f"GDP per Capita: {selected_state_data[5]}")
print(f"Per Capita Personal Income: {selected_state_data[6]}")


#_________________

# Display a bar chart to compare income per capita between the states in the selected region
# Extract data from region_data for visualization

# 'states' will hold a list of state names from 'region_data'
states = [state_data[0] for state_data in region_data]  

# 'income_per_capita' will hold the personal income per capita for each state
income_per_capita = [state_data[6] for state_data in region_data]  

# Creating bar chart for income per capita by state
plt.figure(figsize=(10, 6))  

# Plotting 'states' on the x-axis and 'income_per_capita' on the y-axis as a bar chart
plt.bar(states, income_per_capita)  

# Label the x-axis and y-axis
plt.xlabel("States")
plt.ylabel("Income per Capita (USD)")

# Set a title, using 'selected_region' to make the title specific to the chosen region
plt.title(f"Income per Capita by State in {selected_region}")

# Rotating the x-axis labels to make them more readable, especially if there are many states
plt.xticks(rotation=45, ha='right')

# Displaying the bar chart
plt.show()


#_________________

# Now I want to display the chosen state's proportion of the Region's total GDP 
# This will help us understand the proportion each state contributes to the regional GDP
total_region_gdp = sum(state_data[3] for state_data in region_data)  # Index 3 is the GDP

# Extract GDP values and state names for the pie chart
state_names = [state_data[0] for state_data in region_data]  # List of state names
state_gdp_values = [state_data[3] for state_data in region_data]  # List of GDP values for each state

# Making a list of colors to visually highlight the selected state
# The selected state will be colored in "royalblue", while other states are "lightgrey"
colors = ["lightgrey" if state != selected_state_data[0] else "royalblue" for state in state_names]

# Plotting a pie chart to show the GDP share of each state within the region
plt.figure(figsize=(8, 8)) 

# Plotting the pie chart with state GDP values and labels
# 'autopct' shows the percentage value on each slice, formatted to one decimal place
# 'colors' applies the color scheme, and 'startangle' rotates the chart for a better initial view
plt.pie(state_gdp_values, labels=state_names, autopct='%1.1f%%', colors=colors, startangle=140)

# Setting title for the pie chart, using 'selected_state_data[0]' to display the selected state
# This highlights the selected state's share of total GDP in the title for clarity
plt.title(f"{selected_state_data[0]}'s Share of Total GDP in the {selected_region} Region")

# Display pie chart
plt.show()


