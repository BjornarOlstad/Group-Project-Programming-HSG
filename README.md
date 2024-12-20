# Group-Project-Programming-HSG

**Assignment Overview**

This assignment focuses on the design, implementation and testing of Python programs to process data files and extract meaningful information from them.

We use the dataset called State_Data.csv. The source can be found here: https://drive.google.com/drive/u/0/folders/1JeNy2JQVfmSzIy8ZJiwqECWJ7rFWweMZ 

The document Project.02.docx serves as an inspiration for this project, but we have made some changes. 

**Execution**

Download the entire folder from git. It contains the python file for task 1-6, the main file, a folder with the dataset and the readme file.

The pycache folder can be ignored.

To run the program, open and run the main.py file. 

**Task 1** 

Inspired by Task 2 in Project.02 docx, this code is designed to load, filter, and analyze economic data for U.S. states, allowing the user to select a region and then a specific state within that region. The code begins by loading a dataset containing information like state name, region, population, GDP, and personal income. After loading, the data is converted into a list structure where each entry represents a state, with values adjusted to actual numbers for easier calculations.

The user is first prompted to select a region, after which the code filters out states belonging to that specific region and calculates additional metrics like GDP per capita and personal income per capita for each state. The user then selects a specific state from this filtered list. To ensure accuracy, the code validates inputs, allowing only valid region and state names.

Once a state is chosen, the code displays key economic data for that state, including population, GDP, personal income, and the calculated per capita values. Additionally, the code generates two visualizations to help the user better understand the state’s economic standing within its region. A bar chart displays income per capita across all states in the selected region, allowing for easy comparison of income distribution. Furthermore, a pie chart highlights the chosen state’s share of the region’s total GDP, visually emphasizing its economic contribution compared to other states in the region.

An overview of lists and what they contain is provided as follows:
data_list: Holds all state data.
state_data: Represents one state's data within loops.
result and region_data: Filtered lists for the selected region.
valid_regions and valid_states: Sets of unique region and state names.
selected_state_data: Detailed data for the user-selected state.

**Task 2** 

This regression code analyzes the relationship between population and GDP across U.S. states to see if population size can predict economic output. It first splits the data into training and testing sets to validate the model’s performance, then fits a linear regression model on the training data. Using Mean Squared Error (MSE) and R² score, the model’s accuracy is assessed by comparing predicted GDP values with actual values in the test set. A scatter plot displays the actual data points, with the regression line overlaid to visually represent the model’s interpretation of the relationship. This approach provides insights into how well population size correlates with GDP and highlights the strength of this linear relationship.

**Task 3** 

This correlation analysis code allows users to select two parameters from a dataset of U.S. states to examine the relationship between them. The user is prompted to choose two different columns from options such as Population, GDP, Personal Income, Subsidies, Compensation of Employees, and Tax on Production/Imports. The code then calculates the correlation coefficient between the selected parameters to quantify the strength and direction of their relationship. A scatter plot is generated to visually represent the data points, with the x-axis and y-axis labeled according to the chosen parameters. The plot provides a clear visual interpretation of how the two variables are related, helping to identify any potential linear relationships.

Explanation of Correlation Coefficients:
- Correlation of 1: A correlation coefficient of 1 indicates a perfect positive linear relationship between two variables. This means that as one variable increases, the other variable also increases in a perfectly linear manner. In a scatter plot, the data points would form a straight line with a positive slope.

- Correlation of 0: A correlation coefficient of 0 indicates no linear relationship between two variables. This means that changes in one variable do not predict changes in the other variable. In a scatter plot, the data points would be scattered randomly with no discernible pattern or trend.

- Correlation of -1: A correlation coefficient of -1 indicates a perfect negative linear relationship between two variables. This means that as one variable increases, the other variable decreases in a perfectly linear manner. In a scatter plot, the data points would form a straight line with a negative slope.

**Task 4** 

-- 1 --

This code generates heatmaps to provide a clear and concise comparison of key economic indicators across U.S. states. The dataset, which includes metrics such as population, GDP, and personal income, is processed and sorted to ensure the visualizations are both accurate and intuitive.

Each heatmap highlights a single metric, allowing users to easily compare states. States are dynamically sorted by their values within each metric, ensuring that the visualizations emphasize the most significant differences. A red-orange color gradient enhances readability, while numeric annotations with one decimal precision provide clarity.

Features eatures:
- Sorted Visualizations: States are ranked by their values in each heatmap, making it easy to identify top and bottom performers.
- Side-by-Side Comparisons: Multiple heatmaps are displayed in a grid layout, allowing users to compare metrics like population, GDP, and income simultaneously.

-- 2 --

This code performs a clustering analysis to group U.S. states based on their GDP and personal income. Using KMeans clustering, the states are categorized into four distinct clusters, providing insights into their economic similarities and differences. 

A scatterplot visualizes the clusters by plotting GDP against personal income, with each cluster highlighted in a different color. The scatterplot also includes annotations in the legend to indicate the number of states in each cluster, making the distribution clear at a glance.

To further analyze the clusters, the code generates boxplots for variables like GDP, personal income, and population. These boxplots, arranged in a 2x2 grid, provide a detailed view of how these variables are distributed within each cluster, highlighting economic disparities and patterns across states.


**Task 5** 

The program is a data analysis tool designed to enable interactive exploration of state-level economic data. It combines data processing, user-friendly graphical interfaces, and visualization to offer a seamless experience for analyzing data.

At its core, the program loads a dataset containing detailed metrics about various U.S. states, such as population, GDP, personal income, and related economic indicators. Users can interact with the program via graphical dropdown menus to select specific regions and attributes of interest. The program filters the data to focus on the selected region and enriches it by calculating derived metrics like GDP per capita and income per capita.

Once the data is processed, users can choose specific attributes to compare, and the program generates an interactive scatter plot. This plot visually represents relationships between the selected metrics, with state-level annotations that make it easy to interpret. Through this visualization, users gain deeper insights into the economic characteristics and performance of states within the chosen region.

The combination of intuitive interfaces, rich data manipulation, and clear visual outputs makes the program an engaging tool for exploring economic data in a meaningful way.

**Task 6** 

This code offers some visualization on the analysis of economic data for US states. Firstly, it calculates per capital metrics (GDP per capita and Personal Income per capita are derived from the GDP, income & population data in the file). Secondly, it generates different charts to visualize the data and offer additional insights. A bar chart visualizes the average GDP per capita per region (Far East, Great Lakes, Mideast, NE, Plains, Rocky Mountains, SE, SW). The pie chart on the other hand shows the population distribution across the regions that were just specified. Lastly, the scatter plot, shows GDP against pupation on a state-basis. The region-based scatter plot gives the user the chance to make an in-depth analysis (specific region or all states) —> therefore, the user has to select two metrics for the X any Y axis, that want to be analyzed.
