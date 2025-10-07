




def main():
    while True:
        print("\n====== 🛒 Market Inventory Menu ======")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("👋 Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid Option. Please enter a number between 1 and 6")