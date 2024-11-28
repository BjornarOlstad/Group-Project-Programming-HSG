# menu.py

# Import tasks from their respective modules
from task1 import task1
from task2 import task2
from task3 import task3
from task4_1 import task_1
from task4_2 import task_2
from task5 import task5
#from task6 import task6

def main_menu():
    
# Displays a menu and allows the user to select a task to execute.
# The menu loops until the user selects "Exit".
    
    while True:
        # Print the main menu options
        print("\nMain Menu")  # Adding a blank line before the menu for readability
        print("1. Task 1: Data Analysis and Visualization")
        print("2. Task 2: Regression Analysis")
        print("3. Task 3: Correlation Analysis and Visualization")
        print("4. Task 4_1: ")
        print("4. Task 4_2: ")
        print("5. Task 5: Region-Based Data Filtering, Analysis, and Visualization")
        print("6. Task 6: ")
        print("7. Exit")  # Exit option
        
        # Get the user's choice as input
        choice = input("Select a task (1-6) og 7 for exit: ")  
        
        # Handle the user's choice
        if choice == "1":
            task1()  # Call Task 1 function
        elif choice == "2":
            task2()  # Call Task 2 function
        elif choice == "3":
            task3()  # Call Task 3 function
        elif choice == "4_1":
            task4_1()  # Call Task 4 function
        elif choice == "4_1":
            task4_2() 
        elif choice == "5":
            task5()  # Call Task 5 function
        #elif choice == "6":
            #task6()  # Call Task 6 function
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
