import tkinter as tk

# Function to read item data from a file and store it in a dictionary
def read_item_data(filename):
    items_data = {}
    with open(filename, 'r') as file:
        for line in file:
            # Splitting each line of the file into category, name, quantity, and price
            category, name, quantity, price = line.strip().split(',')
            # Creating a dictionary for each item with name, quantity, and price
            item = {'name': name, 'quantity': int(quantity), 'price': float(price)}
            # Storing items in a dictionary with categories as keys
            items_data.setdefault(category, []).append(item)
    return items_data

# Function to search for items within a category based on a query
def search_items(items_data, category, query):
    # Creating a new window to display search results
    result_window = tk.Tk()
    result_window.title("Search Results")

    # List to store found items
    found_items = []
    # Iterating through items in the specified category
    for item in items_data.get(category, []):
        # Checking if the query string matches any part of the item name (case insensitive)
        if query.lower() in item['name'].lower():
            found_items.append(item)

    # Displaying search results
    if found_items:
        for i, item in enumerate(found_items):
            # Displaying item details (name, quantity, price) in labels
            tk.Label(result_window, text=f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}").grid(row=i, column=0)
    else:
        # Displaying a message if no items match the query
        tk.Label(result_window, text=f"No items matching '{query}' found in {category.capitalize()}.").grid(row=0, column=0)

# Main function to create the main window and handle user interaction
def main():
    # Read item data from file
    items_in_store = read_item_data('items_data.txt')
    
    # Create main window
    root = tk.Tk()
    root.title("Supermarket")

    # Create category selection frame
    category_frame = tk.Frame(root)
    category_frame.grid(row=0, column=0, padx=10, pady=10)

    # Label for category selection
    tk.Label(category_frame, text="Select a category:").grid(row=0, column=0, columnspan=2)

    # List of categories
    categories = ['Vegetables', 'Fruits', 'Dairy Products', 'Meat and Poultry']
    # Creating buttons for each category
    for i, category in enumerate(categories, start=1):
        tk.Button(category_frame, text=category, command=lambda cat=category: show_search_window(cat, items_in_store)).grid(row=i, column=0, pady=5)

    # Button to quit the application
    tk.Button(category_frame, text="Quit", command=root.quit).grid(row=len(categories)+1, column=0, pady=5)

    root.mainloop()

# Function to create a search window for a specific category
def show_search_window(category, items_data):
    search_window = tk.Toplevel()
    search_window.title(f"Search {category.capitalize()}")

    # Label for query entry
    tk.Label(search_window, text=f"What are you looking for in {category.capitalize()}?").grid(row=0, column=0)
    # Entry widget for user input
    query_entry = tk.Entry(search_window)
    query_entry.grid(row=0, column=1)
    # Button to initiate the search
    search_btn = tk.Button(search_window, text="Search", command=lambda: search_items(items_data, category.lower(), query_entry.get()))
    search_btn.grid(row=1, column=0, columnspan=2, pady=5)

# Entry point of the program
if __name__ == "__main__":
    main()
