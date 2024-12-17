def task6():
    """
    Task 6: Visualization Tool
    This code helps to visualize per capita per state data
    """
  
    print("Task Name: Visualization Tool")

    # Import libraries
    import pandas as pd
    import pylab
    import matplotlib.pyplot as plt


# Load the data
data = pd.read_csv('/mnt/data/State_Data.csv')

# Function to calculate GDP per capita and Personal Income per capita
def calculate_per_capita(data):
    data['GDP per capita'] = (data['GDP (billions)'] * 1e9) / (data['Population (millions)'] * 1e6)
    data['Personal Income per capita'] = (data['Personal Income (billions)'] * 1e9) / (data['Population (millions)'] * 1e6)
    return data

# Function to generate summary visualizations
def generate_summary_visualizations(data):
    data = calculate_per_capita(data)
    regions = data['Region'].unique()

    # Visualization 1: Bar chart of GDP per capita by region
    plt.figure(figsize=(10, 6))
    gdp_per_region = data.groupby('Region')['GDP per capita'].mean().sort_values()
    gdp_per_region.plot(kind='bar', color='skyblue')
    plt.title('Average GDP per Capita by Region')
    plt.ylabel('GDP per Capita ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization 2: Pie chart of total population by region
    plt.figure(figsize=(8, 8))
    population_per_region = data.groupby('Region')['Population (millions)'].sum()
    population_per_region.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
    plt.title('Population Distribution by Region')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

    # Visualization 3: Scatter plot of GDP vs Population for all states
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Population (millions)'], data['GDP (billions)'], color='green', alpha=0.7)
    for i, txt in enumerate(data['State']):
        plt.annotate(txt, (data['Population (millions)'].iloc[i], data['GDP (billions)'].iloc[i]))
    plt.title('GDP vs Population for All States')
    plt.xlabel('Population (millions)')
    plt.ylabel('GDP (billions)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to prompt user for x and y values and plot the scatter plot
def plot_data_for_region(data):
    valid_columns = {
        "Pop": "Population (millions)",
        "GDP": "GDP (billions)",
        "PI": "Personal Income (billions)",
        "Sub": "Subsidies (millions)",
        "CE": "Comp of Emp (billions)",
        "TPI": "Tax on Prod/Imp (billions)",
        "GDPp": "GDP per capita",
        "Pip": "Personal Income per capita"
    }

    # Format the data to include per capita values
    data = calculate_per_capita(data)
    
    # Prompt for region input
    while True:
        region = input("Enter a region name (or 'all' for all regions): ").strip().lower()
        if region == 'all':
            region_data = data
            break
        elif region in [r.lower() for r in data['Region'].unique()]:
            region_data = data[data['Region'].str.lower() == region]
            break
        else:
            print("Invalid region. Try again.")

    # Prompt for x and y values
    while True:
        try:
            user_input = input("Enter x and y values separated by a space (e.g., Pop GDP): ").strip().split()
            if len(user_input) != 2:
                raise ValueError("Invalid input format. Enter two values separated by a space.")
            x_key, y_key = user_input
            if x_key not in valid_columns or y_key not in valid_columns:
                raise ValueError("Invalid column name(s). Choose from Pop, GDP, PI, Sub, CE, TPI, GDPp, Pip.")
            break
        except ValueError as e:
            print(e)

    # Extract the chosen columns
    x = region_data[valid_columns[x_key]].round(2)
    y = region_data[valid_columns[y_key]].round(2)
    states = region_data['State']

    # Plotting the scatter plot
    pylab.figure(figsize=(10, 6))
    pylab.scatter(x, y, color='blue')
    for i, txt in enumerate(states):
        pylab.annotate(txt, (x.iloc[i], y.iloc[i]))
    pylab.xlabel(valid_columns[x_key])
    pylab.ylabel(valid_columns[y_key])
    pylab.title(f"Scatter Plot of {valid_columns[x_key]} vs {valid_columns[y_key]} in {region.title()} Region")
    pylab.grid(True)
    pylab.show()

# Main execution
if __name__ == "__main__":
    print("Welcome to the State Data Analysis Tool!")
    print("You can plot data for a specific region or all states.")
    generate_summary_visualizations(data)
    plot_data_for_region(data)
