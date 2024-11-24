import pandas as pd
import tkinter as tk
from tkinter import ttk
from tabulate import tabulate
import pylab


def open_csv_file():
    while True:
        try:
            file_name = input("Enter the path to the CSV file: ").strip()
            data = pd.read_csv(file_name)
            print(f"File '{file_name}' loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Please try again.")

def select_region_dropdown(regions):
    root = tk.Tk()
    root.title("Select a Region")

    selected_region = tk.StringVar(value=regions[0])  

    def confirm_selection():
        nonlocal selected_region
        selected_region = region_menu.get()
        root.destroy()

    label = tk.Label(root, text="Please select a region:", font=("Arial", 14))
    label.pack(pady=10)

    region_menu = ttk.Combobox(root, values=regions, textvariable=selected_region, state="readonly", font=("Arial", 12))
    region_menu.pack(pady=10)

    confirm_button = tk.Button(root, text="Confirm", command=confirm_selection, font=("Arial", 12))
    confirm_button.pack(pady=10)

    root.mainloop()

    return selected_region

def select_attributes_dropdown():
    allowed_attributes = [
        "Pop", "GDP", "PI", "Sub", "CE", "TPI", "GDPp", "Pip"
    ]
    
    root = tk.Tk()
    root.title("Select X and Y Attributes")

    x_attr = tk.StringVar(value=allowed_attributes[0])
    y_attr = tk.StringVar(value=allowed_attributes[0])

    def confirm_selection():
        nonlocal x_attr, y_attr
        x_attr = x_menu.get()
        y_attr = y_menu.get()
        root.destroy()

    label_x = tk.Label(root, text="Please select the X attribute:", font=("Arial", 14))
    label_x.pack(pady=5)
    x_menu = ttk.Combobox(root, values=allowed_attributes, textvariable=x_attr, state="readonly", font=("Arial", 12))
    x_menu.pack(pady=5)

    label_y = tk.Label(root, text="Please select the Y attribute:", font=("Arial", 14))
    label_y.pack(pady=5)
    y_menu = ttk.Combobox(root, values=allowed_attributes, textvariable=y_attr, state="readonly", font=("Arial", 12))
    y_menu.pack(pady=5)

    confirm_button = tk.Button(root, text="Confirm", command=confirm_selection, font=("Arial", 12))
    confirm_button.pack(pady=10)

    root.mainloop()

    return x_attr, y_attr

def add_data_columns_to_selected_region(data, selected_region):
    filtered_data = data[data["Region"] == selected_region]

    filtered_data["GDP per capita"] = (filtered_data["GDP (billions)"] * 1e9) / (filtered_data["Population (millions)"] * 1e6)
    filtered_data["Income per capita"] = (filtered_data["Personal Income (billions)"] * 1e9) / (filtered_data["Population (millions)"] * 1e6)

    filtered_data["GDP per capita"] = filtered_data["GDP per capita"].round(2)
    filtered_data["Income per capita"] = filtered_data["Income per capita"].round(2)

    display_columns = [
        "State", "Population (millions)", "GDP (billions)", "Personal Income (billions)", "Subsidies (millions)", 
        "Comp of Emp (billions)", "Tax on Prod/Imp (billions)", 
        "GDP per capita", "Income per capita"
    ]
    filtered_data = filtered_data[display_columns]

    print("\nFiltered Data Table:")
    print(tabulate(filtered_data, headers="keys", tablefmt="fancy_grid", showindex=False))

    return filtered_data

def plot_data_for_selected_region(filtered_data):
    attribute_map = {
        "Pop": "Population (millions)",
        "GDP": "GDP (billions)",
        "PI": "Personal Income (billions)",
        "Sub": "Subsidies (millions)",
        "CE": "Comp of Emp (billions)",
        "TPI": "Tax on Prod/Imp (billions)",
        "GDPp": "GDP per capita",
        "Pip": "Income per capita"
    }
    
    # Select X and Y attributes via dropdown
    x_attr, y_attr = select_attributes_dropdown()

    x = filtered_data[attribute_map[x_attr]].tolist()
    y = filtered_data[attribute_map[y_attr]].tolist()
    states = filtered_data["State"].tolist()

    pylab.scatter(x, y)
    for i, txt in enumerate(states):
        pylab.annotate(txt, (x[i], y[i]))

    pylab.title(f"Scatter Plot: {x_attr} vs {y_attr}")
    pylab.xlabel(attribute_map[x_attr])
    pylab.ylabel(attribute_map[y_attr])
    pylab.show()


if __name__ == "__main__":
    data = open_csv_file()

    required_columns = [
        "State", "Population (millions)", "GDP (billions)", "Personal Income (billions)", "Subsidies (millions)", 
        "Comp of Emp (billions)", "Tax on Prod/Imp (billions)"
    ]
    if not all(col in data.columns for col in required_columns):
        print("Error: Missing required columns in the data. Please check the CSV file format.")
    else:
        regions = [
            "Far_West", "Great_Lakes", "Mideast", "New_England", 
            "Plains", "Rocky_Mountain", "Southeast", "Southwest"
        ]
        selected_region = select_region_dropdown(regions)
        print(f"\nYou selected the region: {selected_region}")

        filtered_data = add_data_columns_to_selected_region(data, selected_region)
        plot_data_for_selected_region(filtered_data)
