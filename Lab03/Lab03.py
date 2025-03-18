def display_menu():
    print("\nMenu:")
    print("1. Add a number to the list")
    print("2. Remove a number from the list")
    print("3. Insert a number at a specific position")
    print("4. Pop a number from the list")
    print("5. Find the sum, average, and maximum of the list")
    print("6. Search for a number in the list")
    print("7. Remove all odd numbers from the list")
    print("8. Exit")


def print_list(lst):
    if len(lst) == 0:
        print("The list is currently empty.")
    else:
        print(f"Current list: {lst}")


def add_number(lst):
    num = input("Enter a number to add: ")
    if num.replace('.', '', 1).isdigit():  # Check if valid number
        lst.append(float(num))
        print("Number added to the list.")
    else:
        print("Invalid input. Please enter a valid number.")


def remove_number(lst):
    num = input("Enter the number to remove: ")
    if num.replace('.', '', 1).isdigit():  
        num = float(num)
        if num in lst:
            lst.remove(num)
            print("Number removed from the list.")
        else:
            print("Error: Number not found in the list.")
    else:
        print("Invalid input. Please enter a valid number.")


def insert_number(lst):
    num = input("Enter the number to insert: ")
    index = input("Enter the index position: ")

    if num.replace('.', '', 1).isdigit() and index.isdigit():
        num = float(num)
        index = int(index)
        if 0 <= index <= len(lst):
            lst.insert(index, num)
            print("Number inserted into the list.")
        else:
            print("Error: Index out of range.")
    else:
        print("Invalid input. Please enter a valid number and index.")


def pop_number(lst):
    if len(lst) == 0:
        print("Error: The list is empty.")
        return
    
    index = input("Enter the index to pop: ")
    
    if index.isdigit():
        index = int(index)
        if 0 <= index < len(lst):
            removed = lst.pop(index)
            print(f"Removed number: {removed}")
        else:
            print("Error: Index out of range.")
    else:
        print("Invalid input. Please enter a valid index.")


def calculate_stats(lst):
    if len(lst) == 0:
        print("Error: The list is empty.")
    else:
        total = sum(lst)
        avg = total / len(lst)
        max_value = max(lst)
        print(f"Sum: {total}, Average: {avg}, Maximum: {max_value}")


def search_number(lst):
    num = input("Enter the number to search: ")
    if num.replace('.', '', 1).isdigit():
        num = float(num)
        if num in lst:
            print(f"Number found at index: {lst.index(num)}")
        else:
            print("Number not found in the list.")
    else:
        print("Invalid input. Please enter a valid number.")


def remove_odds(lst):
    lst[:] = [num for num in lst if num % 2 == 0]
    print("All odd numbers removed from the list.")


def main():
    lst = []
    print("Welcome to the List Operations Program!")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_number(lst)
        elif choice == "2":
            remove_number(lst)
        elif choice == "3":
            insert_number(lst)
        elif choice == "4":
            pop_number(lst)
        elif choice == "5":
            calculate_stats(lst)
        elif choice == "6":
            search_number(lst)
        elif choice == "7":
            remove_odds(lst)
        elif choice == "8":
            print("Thank you for using the List Operations Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

        should_print = input("\nWould you like to print the current list? (yes/no): ").strip().lower()
        if should_print == "yes":
            print_list(lst)


if __name__ == "__main__":
    main()
