# menu.py

# Import tasks from their respective modules
from task1 import task1
from task2 import task2
from task3 import task3
from task4_1 import task4_1
from task4_2 import task4_2
from task5 import task5
from task6 import task6

def main_menu():
    
# Displays a menu and allows the user to select a task to execute.
# The menu loops until the user selects "Exit".
    
    while True:
        # Print the main menu options
        print("\nMain Menu")  # Adding a blank line before the menu for readability
        print("Task 1: Data Analysis and Visualization")
        print("Task 2: Regression Analysis")
        print("Task 3: Correlation Analysis and Visualization")
        print("Task 4.1: Data Visualization - Heatmap")
        print("Task 4.2: Clustering Analysis of Economic Patterns Across Regions")
        print("Task 5: Region-Based Data Filtering, Analysis, and Visualization")
        print("Task 6: Visualization Tool")
        print("7. Exit")  # Exit option
        
        # Get the user's choice as input
        choice = input("Select tasknumber (1-6) or 7 for exit: ")  
        
        # Handle the user's choice
        if choice == "1":
            task1()  
        elif choice == "2":
            task2()  
        elif choice == "3":
            task3()  
        elif choice == "4.1":
            task4_1() 
        elif choice == "4.2":
            task4_2() 
        elif choice == "5":
            task5()  
        elif choice == "6":
            task6() 
        elif choice == "7":
            print("Exiting program. Thanks for using")  # Exit message
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid inputs


  
  #  We have consciously chosen to make a menu script named menu.py the main entry point for this program.
  #  This design decision simplifies the project structure by combining the menu logic 
  #  and the main entry point in one file. While this approach works well for small to 
  #  medium-sized projects, in larger projects, we would consider separating the 
  #  main entry point (main.py) from menu logic for better modularity and maintainability.



if __name__ == "__main__":
   
    main_menu() 
