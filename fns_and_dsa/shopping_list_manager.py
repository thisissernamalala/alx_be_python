
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
           addition = input("Enter item to add: ")
           shopping_list.append(addition)

        elif choice == '2':
            removal = input("Enter item to remove: ")
            count_item = shopping_list.count(removal)
            if count_item <=0:
                print("Item is not in the shopping list")
            else:
                while removal in shopping_list:
                    shopping_list.remove(removal)
        elif choice == '3':
            for x in shopping_list:
                print(x)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





