items_in_store = {
    'vegetables': [
        {'name': 'Carrot', 'quantity': 100, 'price': 0.75},
        {'name': 'Tomato', 'quantity': 80, 'price': 1.00},
        {'name': 'Broccoli', 'quantity': 50, 'price': 1.50}
    ],
    'fruits': [
        {'name': 'Apple', 'quantity': 120, 'price': 0.80},
        {'name': 'Banana', 'quantity': 150, 'price': 0.60},
        {'name': 'Orange', 'quantity': 100, 'price': 0.75}
    ],
    'dairy_products': [
        {'name': 'Milk', 'quantity': 50, 'price': 2.00},
        {'name': 'Cheese', 'quantity': 40, 'price': 3.50},
        {'name': 'Yogurt', 'quantity': 60, 'price': 1.20}
    ],
    'meat_and_poultry': [
        {'name': 'Chicken', 'quantity': 30, 'price': 5.00},
        {'name': 'Beef', 'quantity': 20, 'price': 7.50},
        {'name': 'Pork', 'quantity': 25, 'price': 6.50}
    ]
}
def main():
    print("Welcome to the Shopping Tool!")
    print("Please select a category:")
    print("1. Vegetables")
    print("2. Fruits")
    print("3. Dairy Products")
    print("4. Meat and Poultry")
    

    category_choice = input("Enter the number corresponding to your desired category: ")

  
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

    
    print(f"Searching for '{query}' in Vegetables...")

def search_fruits():
    print("You selected Fruits.")
    query = input("What are you looking for in Fruits? ")

    
    print(f"Searching for '{query}' in Fruits...")

def search_dairy_products():
    print("You selected Dairy Products.")
    query = input("What are you looking for in Dairy Products? ")

   
    print(f"Searching for '{query}' in Dairy Products...")

def search_meat_and_poultry():
    print("You selected Meat and Poultry.")
    query = input("What are you looking for in Meat and Poultry? ")

    
    print(f"Searching for '{query}' in Meat and Poultry...")

if __name__ == "__main__":
    main()
