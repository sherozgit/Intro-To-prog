import tkinter as tk
def read_item_data(filename):
    items_data = {}
    with open(filename, 'r') as file:
        for line in file:
            category, name, quantity, price = line.strip().split(',')
            item = {'name': name, 'quantity': int(quantity), 'price': float(price)}
            items_data.setdefault(category, []).append(item)
    return items_data

def search_items(items_data, category,query):
    result_window = tk.Tk()
    result_window.title("Search Results")

    
    found_items = []
    for item in items_data.get(category, []):
        if query.lower() in item['name'].lower():
            found_items.append(item)

    if found_items:
        for i, item in enumerate(found_items):
            tk.Label(result_window, text=f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}").grid(row=i, column=0)
    else:
        tk.Label(result_window, text=f"No items matching '{query}' found in {category.capitalize()}.").grid(row=0, column=0)

def main():
    items_in_store = read_item_data('items_data.txt')
    root = tk.Tk()
    root.title("Supermarket")
    # Create category selection frame
    category_frame = tk.Frame(root)
    category_frame.grid(row=0, column=0, padx=10, pady=10)
    tk.Label(category_frame, text="Select a category:").grid(row=0, column=0, columnspan=2)

    # Quit button
    tk.Button(category_frame, text="Quit", command=root.quit).grid(row=len(categories)+1, column=0, pady=5)

    categories = ['Vegetables', 'Fruits', 'Dairy Products', 'Meat and Poultry']
    for i, category in enumerate(categories, start=1):
        tk.Button(category_frame, text=category, command=lambda cat=category: show_search_window(cat, items_in_store)).grid(row=i, column=0, pady=5)

    root.mainloop()

    



if __name__ == "__main__":
    main()
