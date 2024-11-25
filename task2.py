def task2():
    """
    Task 2: Regression Analysis 
    This regression code analyzes the relationship between population and GDP across U.S. states
    """
  
    print("Task Name: Regression Analysis")

    # Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("State_Data.csv")

# Function to convert the DataFrame into a list of lists
def load_data_as_list(df):
    data_list = []
    for _, row in df.iterrows():
        state_data = [
            row['State'], 
            row['Region'], 
            row['Population (millions)'] * 1_000_000, 
            row['GDP (billions)'] * 1_000_000_000, 
            row['Personal Income (billions)'] * 1_000_000_000
        ]
        data_list.append(state_data)
    return data_list

# Populate data_list by calling load_data_as_list
data_list = load_data_as_list(df)

# Function to perform regression between population and GDP
def perform_regression(data_list):
    populations = [state_data[2] for state_data in data_list]
    gdps = [state_data[3] for state_data in data_list]

    X = [[pop] for pop in populations]
    y = gdps

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Performance:")
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

    plt.figure(figsize=(10, 6))
    plt.scatter(populations, gdps, color='blue', label='Actual GDP')
    plt.plot(populations, model.predict(X), color='red', linewidth=2, label='Regression Line')
    plt.xlabel("Population")
    plt.ylabel("GDP")
    plt.title("Population vs. GDP Regression Analysis")
    plt.legend()
    plt.show()

    # Run the regression function
    perform_regression(data_list)

    print("Task completed successfully.\n")




