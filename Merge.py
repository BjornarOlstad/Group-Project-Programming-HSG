def task_name():

    print("Task Name: A descriptive name for your task.")
    
    # Place your code here.
    # Ensure the code runs independently within this function.
    
    
    print("Task completed successfully.\n")


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Task 1 Name")
        print("2. Task 2 Name")
        print("3. Task 3 Name")
        print("4. Task 4 Name")
        print("5. Exit")
        
        choice = input("Select a task (1-5): ")
        if choice == "1":
            task1()  # Call the function for Task 1
        elif choice == "2":
            task2()  # Call the function for Task 2
        elif choice == "3":
            task3()  # Call the function for Task 3
        elif choice == "4":
            task4()  # Call the function for Task 4
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
