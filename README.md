# Group-Project-Programming-HSG

**Assignment Overview**
This assignment focuses on the design, implementation and testing of Python programs to process data files and extract meaningful information from them.
We use the dataset called State_Data.csv. The source can be found here: https://drive.google.com/drive/u/0/folders/1JeNy2JQVfmSzIy8ZJiwqECWJ7rFWweMZ 
The document Project.02.docx serves as an inspiration for this project, but we have made some changes. 

**Task 1** (Björnar)
Inspired by Task 2 in Project.02 docx, this code is designed to load, filter, and analyze economic data for U.S. states, allowing the user to select a region and then a specific state within that region. The code begins by loading a dataset containing information like state name, region, population, GDP, and personal income. After loading, the data is converted into a list structure where each entry represents a state, with values adjusted to actual numbers for easier calculations.

The user is first prompted to select a region, after which the code filters out states belonging to that specific region and calculates additional metrics like GDP per capita and personal income per capita for each state. The user then selects a specific state from this filtered list. To ensure accuracy, the code validates inputs, allowing only valid region and state names.

Once a state is chosen, the code displays key economic data for that state, including population, GDP, personal income, and the calculated per capita values. Additionally, the code generates two visualizations to help the user better understand the state’s economic standing within its region. A bar chart displays income per capita across all states in the selected region, allowing for easy comparison of income distribution. Furthermore, a pie chart highlights the chosen state’s share of the region’s total GDP, visually emphasizing its economic contribution compared to other states in the region.

