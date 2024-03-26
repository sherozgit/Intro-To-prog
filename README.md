def read_item_data(filename):
    items_data = {}
    with open(filename, 'r') as file:
        for line in file:
            category, name, quantity, price = line.strip().split(',')
            item = {'name': name, 'quantity': int(quantity), 'price': float(price)}
            items_data.setdefault(category, []).append(item)
    return items_data
def main():
    items_in_store = read_item_data('items_data.txt')
    print("Welcome to the Shopping Tool!")

    while True:
    print("Please select a category:")
        print("1. Vegetables")
        print("2. Fruits")
        print("3. Dairy Products")
        print("4. Meat and Poultry")
        print("5. Quit")
        
       
        category_choice = input("Enter the number corresponding to your desired category (or '5' to quit): ")

        
        if category_choice == '5':
            print("Thank you for using the Shopping Tool. Goodbye!")
            break
        elif category_choice in ['1', '2', '3', '4']:
            category_mapping = {'1': 'vegetables', '2': 'fruits', '3': 'dairy_products', '4': 'meat_and_poultry'}
            search_items(items_in_store, category_mapping[category_choice])
        else:
            print("Invalid choice. Please select a valid category.")
    
    print("Please select a category:")
    print("1. Vegetables")
    print("2. Fruits")
    print("3. Dairy Products")
    print("4. Meat and Poultry")
    

    category_choice = input("Enter the number corresponding to your desired category: ")

  
    if category_choice in ['1', '2', '3', '4']:
        category_mapping = {'1': 'vegetables', '2': 'fruits', '3': 'dairy_products','4': 'meat_and_poultry'}
        search_items(items_in_store, category_mapping[category_choice])
    else:
        print("Invalid choice. Please select a valid category.")
def search_items(items_data, category):
    print(f"You selected {category.capitalize()}.")
    query = input(f"What are you looking for in {category.capitalize()}? ")

    # Implement search logic for the specified category based on user's query
    found_items = []
    for item in items_data.get(category, []):
        if query.lower() in item['name'].lower():
            found_items.append(item)

    if found_items:
        print("Found items:")
        for item in found_items:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")
    else:
        print(f"No items matching '{query}' found in {category.capitalize()}.")


if __name__ == "__main__":
    main()
