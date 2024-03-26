def main():
    print("Welcome to the Shopping Tool!")
    print("Please select a category:")
    print("1. Vegetables")
    print("2. Fruits")
    print("3. Dairy Products")
    print("4. Meat and Poultry")
    
    # Get user's choice
    category_choice = input("Enter the number corresponding to your desired category: ")

    # Handle user's choice
    if category_choice == '1':
        search_vegetables()
    elif category_choice == '2':
        search_fruits()
    elif category_choice == '3':
        search_dairy_products()
    elif category_choice == '4':
        search_meat_and_poultry()
    else:
        print("Invalid choice. Please select a valid category.")

def search_vegetables():
    print("You selected Vegetables.")
    query = input("What are you looking for in Vegetables? ")

    # Implement search logic for Vegetables category based on user's query
    print(f"Searching for '{query}' in Vegetables...")

def search_fruits():
    print("You selected Fruits.")
    query = input("What are you looking for in Fruits? ")

    # Implement search logic for Fruits category based on user's query
    print(f"Searching for '{query}' in Fruits...")

def search_dairy_products():
    print("You selected Dairy Products.")
    query = input("What are you looking for in Dairy Products? ")

    # Implement search logic for Dairy Products category based on user's query
    print(f"Searching for '{query}' in Dairy Products...")

def search_meat_and_poultry():
    print("You selected Meat and Poultry.")
    query = input("What are you looking for in Meat and Poultry? ")

    # Implement search logic for Meat and Poultry category based on user's query
    print(f"Searching for '{query}' in Meat and Poultry...")

if __name__ == "__main__":
    main()
