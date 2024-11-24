# menu.py

# Import tasks from their respective modules
from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5
from task6 import task6

def main_menu():
    
# Displays a menu and allows the user to select a task to execute.
# The menu loops until the user selects "Exit".
    
    while True:
        # Print the main menu options
        print("\nMain Menu")  # Adding a blank line before the menu for readability
        print("1. Task 1: Data Analysis")
        print("2. Task 2: Visualization")
        print("3. Task 3: Correlation Analysis")
        print("4. Task 4: Clustering Analysis")
        print("5. Task 5: Statistical Analysis")
        print("6. Task 6: Advanced Modeling")
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
        elif choice == "4":
            task4()  # Call Task 4 function
        elif choice == "5":
            task5()  # Call Task 5 function
        elif choice == "6":
            task6()  # Call Task 6 function
        elif choice == "7":
            print("Exiting program.")  # Exit message
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid inputs


  
  #  We have consciously chosen to make menu.py the main entry point for this program.
  #  This design decision simplifies the project structure by combining the menu logic 
  #  and the main entry point in one file. While this approach works well for small to 
  #  medium-sized projects, in larger projects, we would consider separating the 
  #  main entry point (main.py) from menu logic for better modularity and maintainability.



if __name__ == "__main__":
   
    main_menu() 