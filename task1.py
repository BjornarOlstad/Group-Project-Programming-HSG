def task1():
    """
    Task 1: Data Analysis and Visualization.
    This task allows the user to select a region and a state to analyze data,
    and provides visualizations such as bar and pie charts.
    """
    
    print("Task 1: Data Analysis and Visualization")

    # Import libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the dataset 
    df = pd.read_csv("data/State_Data.csv")

    # Function to convert the DataFrame into a list of lists
    # Purpose: To convert the dataset from a dataframe to a structured list for easier filtering and manipulation
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
        
        # Return the populated data_list with all states data
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
    # Purpose: To get a valid region from the user based on available data
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
    # Purpose: To prompt the user for a specific state within the chosen region, validate the input, and handle formatting issues.
    def get_valid_state(region_data):
        # Extract state names from region_data (first element in each list) and strip any extra spaces
        valid_states = {state_data[0].strip() for state_data in region_data}  
        
        # Loop to continually prompt the user until a valid state is entered
        while True:
            # Prompt user to select a state within the region and remove any leading/trailing spaces from the input
            state = input(f"Enter a state from the following list: {', '.join(valid_states)}\n").strip()
            
            # Check if the entered state matches a valid state in the region
            for state_data in region_data:
                # Compare the input with the state names in region_data
                if state.lower() == state_data[0].strip().lower():
                    # If a match is found, return the corresponding state data
                    return state_data
            
            # If no match is found, notify the user and prompt again
            print("Invalid state name. Please try again.")


    # Main program execution
    # Step 1: Load data as a list of lists
    data_list = load_data_as_list(df)  # Call load_data_as_list with the loaded dataframe

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

    # Visualization logic continues unchanged...
    states = [state_data[0] for state_data in region_data]  
    income_per_capita = [state_data[6] for state_data in region_data]  

    plt.figure(figsize=(10, 6))  
    plt.bar(states, income_per_capita)  
    plt.xlabel("States")
    plt.ylabel("Income per Capita (USD)")
    plt.title(f"Income per Capita by State in {selected_region}")
    plt.xticks(rotation=45, ha='right')
    plt.show()

    total_region_gdp = sum(state_data[3] for state_data in region_data) 
    state_names = [state_data[0] for state_data in region_data]
    state_gdp_values = [state_data[3] for state_data in region_data]  
    colors = ["lightgrey" if state != selected_state_data[0] else "royalblue" for state in state_names]

    plt.figure(figsize=(8, 8)) 
    plt.pie(state_gdp_values, labels=state_names, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(f"{selected_state_data[0]}'s Share of Total GDP in the {selected_region} Region")
    plt.show()

    print("Task completed successfully.\n")

task1()
