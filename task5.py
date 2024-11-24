def task5():

    print("Task Name: Region-Based Data Filtering, Analysis, and Visualization")
    
    # Import required libraries
    import pandas as pd
    import tkinter as tk
    from tkinter import ttk
    from tabulate import tabulate
    import pylab

    # Function to create a dropdown menu for selecting a region
    def select_region_dropdown(regions):
        # Initialize the tkinter root window
        root = tk.Tk()
        root.title("Select a Region")

        # Default selection for the dropdown
        selected_region = tk.StringVar(value=regions[0])  

        # Function to handle confirmation of the selected region
        def confirm_selection():
            nonlocal selected_region
            selected_region = region_menu.get()
            root.destroy()

        # Label to guide the user
        label = tk.Label(root, text="Please select a region:", font=("Arial", 14))
        label.pack(pady=10)

        # Dropdown menu for region selection
        region_menu = ttk.Combobox(root, values=regions, textvariable=selected_region, state="readonly", font=("Arial", 12))
        region_menu.pack(pady=10)

        # Button to confirm the selection
        confirm_button = tk.Button(root, text="Confirm", command=confirm_selection, font=("Arial", 12))
        confirm_button.pack(pady=10)

        root.mainloop()

        # Return the selected region
        return selected_region

    # Function to create dropdown menus for selecting attributes to plot
    def select_attributes_dropdown():
        # List of allowed attributes for selection
        allowed_attributes = [
        "Population",
        "GDP",
        "Personal Income",
        "Subsidies",
        "Comp of Emp",
        "Tax on Prod/Imp",
        "GDP per capita",
        "Income per capita"
        ]
        
        # Initialize the tkinter root window
        root = tk.Tk()
        root.title("Select X and Y Attributes")

        # Default selections for X and Y attributes
        x_attr = tk.StringVar(value=allowed_attributes[0])
        y_attr = tk.StringVar(value=allowed_attributes[0])

        # Function to handle confirmation of selected attributes
        def confirm_selection():
            nonlocal x_attr, y_attr
            x_attr = x_menu.get()
            y_attr = y_menu.get()
            root.destroy()

        # Label and dropdown menu for selecting the X attribute
        label_x = tk.Label(root, text="Please select the X attribute:", font=("Arial", 14))
        label_x.pack(pady=5)
        x_menu = ttk.Combobox(root, values=allowed_attributes, textvariable=x_attr, state="readonly", font=("Arial", 12))
        x_menu.pack(pady=5)

        # Label and dropdown menu for selecting the Y attribute
        label_y = tk.Label(root, text="Please select the Y attribute:", font=("Arial", 14))
        label_y.pack(pady=5)
        y_menu = ttk.Combobox(root, values=allowed_attributes, textvariable=y_attr, state="readonly", font=("Arial", 12))
        y_menu.pack(pady=5)

        # Button to confirm the selection
        confirm_button = tk.Button(root, text="Confirm", command=confirm_selection, font=("Arial", 12))
        confirm_button.pack(pady=10)

        root.mainloop()

        # Return the selected X and Y attributes
        return x_attr, y_attr

    # Function to filter data for the selected region and add derived columns
    def add_data_columns_to_selected_region(data, selected_region):
        # Filter the data for the specified region
        filtered_data = data[data["Region"] == selected_region]

        # Add derived columns: GDP per capita and Income per capita
        filtered_data["GDP per capita"] = (filtered_data["GDP (billions)"] * 1e9) / (filtered_data["Population (millions)"] * 1e6)
        filtered_data["Income per capita"] = (filtered_data["Personal Income (billions)"] * 1e9) / (filtered_data["Population (millions)"] * 1e6)

        # Round the derived columns to 2 decimal places
        filtered_data["GDP per capita"] = filtered_data["GDP per capita"].round(2)
        filtered_data["Income per capita"] = filtered_data["Income per capita"].round(2)

        # Define the columns to display
        display_columns = [
            "State", "Population (millions)", "GDP (billions)", "Personal Income (billions)", "Subsidies (millions)", 
            "Comp of Emp (billions)", "Tax on Prod/Imp (billions)", 
            "GDP per capita", "Income per capita"
        ]
        filtered_data = filtered_data[display_columns]

        # Print the filtered data in a tabular format
        print("\nFiltered Data Table:")
        print(tabulate(filtered_data, headers="keys", tablefmt="fancy_grid", showindex=False))

        # Return the filtered data
        return filtered_data

    # Function to plot data for the selected region
    def plot_data_for_selected_region(filtered_data):
        # Map short attribute codes to their full column names  
        attribute_map = {
            "Population": "Population (millions)",
            "GDP": "GDP (billions)",
            "Personal Income": "Personal Income (billions)",
            "Subsidies": "Subsidies (millions)",
            "Comp of Emp": "Comp of Emp (billions)",
            "Tax on Prod/Imp": "Tax on Prod/Imp (billions)",
            "GDP per capita": "GDP per capita",
            "Income per capita": "Income per capita"
        }

        # Select X and Y attributes via dropdown
        x_attr, y_attr = select_attributes_dropdown()

        # Retrieve data for the selected attributes
        x = filtered_data[attribute_map[x_attr]].tolist()
        y = filtered_data[attribute_map[y_attr]].tolist()
        states = filtered_data["State"].tolist()

        # Create a scatter plot of the selected attributes
        pylab.scatter(x, y)
        for i, txt in enumerate(states):
            pylab.annotate(txt, (x[i], y[i]))

        # Add plot title and labels
        pylab.title(f"Scatter Plot: {x_attr} vs {y_attr}")
        pylab.xlabel(attribute_map[x_attr])
        pylab.ylabel(attribute_map[y_attr])
        pylab.show()

    
    '''    Main program execution    '''

    # Load the data from a CSV file   
    data = pd.read_csv("data/State_Data.csv")

    # Define available regions for selection
    regions = [
        "Far_West", "Great_Lakes", "Mideast", "New_England", 
        "Plains", "Rocky_Mountain", "Southeast", "Southwest"
    ]
    
    # Allow user to select a region
    selected_region = select_region_dropdown(regions)
    print(f"\nYou selected the region: {selected_region}")

    # Filter the data and add derived columns for the selected region
    filtered_data = add_data_columns_to_selected_region(data, selected_region)
    
    # Plot data for the selected region
    plot_data_for_selected_region(filtered_data)
    
    
    print("Task completed successfully.\n")
 
