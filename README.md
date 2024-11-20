# Group-Project-Programming-HSG

**Assignment Overview**

This assignment focuses on the design, implementation and testing of Python programs to process data files and extract meaningful information from them.

We use the dataset called State_Data.csv. The source can be found here: https://drive.google.com/drive/u/0/folders/1JeNy2JQVfmSzIy8ZJiwqECWJ7rFWweMZ 

The document Project.02.docx serves as an inspiration for this project, but we have made some changes. 

**Task 1** (Björnar)

Inspired by Task 2 in Project.02 docx, this code is designed to load, filter, and analyze economic data for U.S. states, allowing the user to select a region and then a specific state within that region. The code begins by loading a dataset containing information like state name, region, population, GDP, and personal income. After loading, the data is converted into a list structure where each entry represents a state, with values adjusted to actual numbers for easier calculations.

The user is first prompted to select a region, after which the code filters out states belonging to that specific region and calculates additional metrics like GDP per capita and personal income per capita for each state. The user then selects a specific state from this filtered list. To ensure accuracy, the code validates inputs, allowing only valid region and state names.

Once a state is chosen, the code displays key economic data for that state, including population, GDP, personal income, and the calculated per capita values. Additionally, the code generates two visualizations to help the user better understand the state’s economic standing within its region. A bar chart displays income per capita across all states in the selected region, allowing for easy comparison of income distribution. Furthermore, a pie chart highlights the chosen state’s share of the region’s total GDP, visually emphasizing its economic contribution compared to other states in the region.

An overview of lists and what they contain is provided as follows:
data_list: Holds all state data.
state_data: Represents one state's data within loops.
result and region_data: Filtered lists for the selected region.
valid_regions and valid_states: Sets of unique region and state names.
selected_state_data: Detailed data for the user-selected state.

**Task 2** (Andreas)

This regression code analyzes the relationship between population and GDP across U.S. states to see if population size can predict economic output. It first splits the data into training and testing sets to validate the model’s performance, then fits a linear regression model on the training data. Using Mean Squared Error (MSE) and R² score, the model’s accuracy is assessed by comparing predicted GDP values with actual values in the test set. A scatter plot displays the actual data points, with the regression line overlaid to visually represent the model’s interpretation of the relationship. This approach provides insights into how well population size correlates with GDP and highlights the strength of this linear relationship.

**Task 3** (Larissa)

This correlation analysis code allows users to select two parameters from a dataset of U.S. states to examine the relationship between them. The user is prompted to choose two different columns from options such as Population, GDP, Personal Income, Subsidies, Compensation of Employees, and Tax on Production/Imports. The code then calculates the correlation coefficient between the selected parameters to quantify the strength and direction of their relationship. A scatter plot is generated to visually represent the data points, with the x-axis and y-axis labeled according to the chosen parameters. The plot provides a clear visual interpretation of how the two variables are related, helping to identify any potential linear relationships.

Explanation of Correlation Coefficients:
- Correlation of 1: A correlation coefficient of 1 indicates a perfect positive linear relationship between two variables. This means that as one variable increases, the other variable also increases in a perfectly linear manner. In a scatter plot, the data points would form a straight line with a positive slope.

- Correlation of 0: A correlation coefficient of 0 indicates no linear relationship between two variables. This means that changes in one variable do not predict changes in the other variable. In a scatter plot, the data points would be scattered randomly with no discernible pattern or trend.

- Correlation of -1: A correlation coefficient of -1 indicates a perfect negative linear relationship between two variables. This means that as one variable increases, the other variable decreases in a perfectly linear manner. In a scatter plot, the data points would form a straight line with a negative slope.

**Task** (Phil)
-- 1 --
This code generates heatmaps to provide a clear and concise comparison of key economic indicators across U.S. states. The dataset, which includes metrics such as population, GDP, and personal income, is processed and sorted to ensure the visualizations are both accurate and intuitive.

Each heatmap highlights a single metric, allowing users to easily compare states. States are dynamically sorted by their values within each metric, ensuring that the visualizations emphasize the most significant differences. A red-orange color gradient enhances readability, while numeric annotations with one decimal precision provide clarity.

Features eatures:
- Sorted Visualizations: States are ranked by their values in each heatmap, making it easy to identify top and bottom performers.
- Side-by-Side Comparisons: Multiple heatmaps are displayed in a grid layout, allowing users to compare metrics like population, GDP, and income simultaneously.

**-- 2 --**
