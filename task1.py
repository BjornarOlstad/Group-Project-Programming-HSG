def task1():
    """
    Task 1: Data Analysis and Visualization
    This task performs data analysis on the state dataset, allowing the user to filter by region and state,
    and then displays per capita income, GDP, and visualizations.
    """
    print("Task Name: Data Analysis and Visualization")
    
    # Import libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the dataset
    df = pd.read_csv("data/State_Data.csv")

    # Function to convert the DataFrame into a list of lists
    def load_data_as_list(df):
        data_list = []
        for _, row in df.iterrows():
            state_data = [
                row['State'],                            # State name
                row['Region'],                           # Region
                row['Population (millions)'] * 1_000_000,  # Population
                row['GDP (billions)'] * 1_000_000_000,     # GDP
                row['Personal Income (billions)'] * 1_000_000_000  # Income
            ]
            data_list.append(state_data)
        return data_list

    # Function to calculate per capita values for a region
    def calculate_per_capita_list(data_list, region):
        result = []

        for state_data in data_list:
            state, state_region, population, gdp, income = state_data
            if state_region.lower() == region.lower():
                gdp_per_capita = gdp / population
                income_per_capita = income / population
                result.append([
                    state, state_region, population, gdp, income, gdp_per_capita, income_per_capita
                ])
        return result

    # Prompt for a valid region
    def get_valid_region(data_list):
        valid_regions = {state_data[1] for state_data in data_list}
        while True:
            region = input(f"Enter a region from the following list: {', '.join(valid_regions)}\n").strip()
            if region in valid_regions:
                return region
            print("Invalid region name. Please try again.")

    # Prompt for a valid state within the region
    def get_valid_state(region_data):
        valid_states = {state_data[0] for state_data in region_data}
        while True:
            state = input(f"Enter a state from the following list: {', '.join(valid_states)}\n").strip()
            if state in valid_states:
                for state_data in region_data:
                    if state_data[0] == state:
                        return state_data
            print("Invalid state name. Please try again.")

    # Step 1: Load data
    data_list = load_data_as_list(df)

    # Step 2: Get region and state
    selected_region = get_valid_region(data_list)
    region_data = calculate_per_capita_list(data_list, selected_region)
    selected_state_data = get_valid_state(region_data)

    # Display state details
    print("\nInformation for the selected state:")
    print(f"State: {selected_state_data[0]}")
    print(f"Region: {selected_state_data[1]}")
    print(f"Population: {selected_state_data[2]}")
    print(f"GDP: {selected_state_data[3]}")
    print(f"Personal Income: {selected_state_data[4]}")
    print(f"GDP per Capita: {selected_state_data[5]}")
    print(f"Per Capita Personal Income: {selected_state_data[6]}")

    # Visualization: Bar chart of income per capita
    states = [state_data[0] for state_data in region_data]
    income_per_capita = [state_data[6] for state_data in region_data]
    plt.figure(figsize=(10, 6))
    plt.bar(states, income_per_capita)
    plt.xlabel("States")
    plt.ylabel("Income per Capita (USD)")
    plt.title(f"Income per Capita by State in {selected_region}")
    plt.xticks(rotation=45, ha='right')
    plt.show()

    # Visualization: Pie chart of GDP contribution
    total_region_gdp = sum(state_data[3] for state_data in region_data)
    state_names = [state_data[0] for state_data in region_data]
    state_gdp_values = [state_data[3] for state_data in region_data]
    colors = ["lightgrey" if state != selected_state_data[0] else "royalblue" for state in state_names]
    plt.figure(figsize=(8, 8))
    plt.pie(state_gdp_values, labels=state_names, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(f"{selected_state_data[0]}'s Share of Total GDP in the {selected_region} Region")
    plt.show()
    
    print("Task completed successfully.\n")


