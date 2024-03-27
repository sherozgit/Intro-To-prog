import tkinter as tk

# Global variable to store the items selected by the user
selected_items = []

# Function to read item data from a file and store it in a nested dictionary
def read_item_data(filename):
    items_data = {}
    with open(filename, 'r') as file:
        for line in file:
            # Splitting each line of the file into category, name, quantity, and price
            category, name, quantity, price = line.strip().split(',')
            # Creating a nested dictionary to store item details
            item = {'quantity': int(quantity), 'price': float(price)}
            # Check if the category already exists in items_data
            if category in items_data:
                items_data[category][name] = item
            else:
                items_data[category] = {name: item}
    return items_data

# Function to search for items within a category based on a query
def search_items(items_data, category, query):
    # Creating a new window to display search results
    result_window = tk.Tk()
    result_window.title("Search Results")

    # List to store found items
    found_items = []
    # Iterating through items in the specified category
    for item_name, item_details in items_data.get(category, {}).items():
        # Checking if the query string matches any part of the item name (case insensitive)
        if query.lower() in item_name.lower():
            found_items.append((item_name, item_details))

    # Displaying search results
    if found_items:
        for i, (item_name, item_details) in enumerate(found_items):
            # Displaying item details (name, quantity, price) in labels
            tk.Label(result_window, text=f"Name: {item_name}, Quantity: {item_details['quantity']}, Price: ${item_details['price']:.2f}").grid(row=i, column=0)
            # Button to buy the item
            buy_btn = tk.Button(result_window, text="Buy", command=lambda name=item_name, details=item_details: buy_item(name, details))
            buy_btn.grid(row=i, column=1)
    else:
        # Displaying a message if no items match the query
        tk.Label(result_window, text=f"No items matching '{query}' found in {category.capitalize()}.").grid(row=0, column=0)

# Function to handle buying items
def buy_item(name, details):
    selected_items.append((name, details))
    print(f"{name} added to cart.")

# Function to handle paying for the selected items
def pay():
    total_amount = sum(item['price'] for _, item in selected_items)
    print(f"Total amount to pay: ${total_amount:.2f}")

# Main function to create the main window and handle user interaction
def main():
    # Read item data from file
    items_in_store = read_item_data('items_data.txt')
    
    # Create main window
    root = tk.Tk()
    root.title("Supermarket")
    root.configure(bg='lightgray')

    # Create category selection frame
    category_frame = tk.Frame(root, bg='lightgray')  # Specify background color for the frame
    category_frame.grid(row=0, column=0, padx=10, pady=10)

    # Label for category selection
    tk.Label(category_frame, text="Select a category:").grid(row=0, column=0, columnspan=2)

    # List of categories
    categories = ['Vegetables', 'Fruits', 'Dairy Products', 'Meat and Poultry']
    # Creating buttons for each category
    for i, category in enumerate(categories, start=1):
        btn = tk.Button(category_frame, text=category, bg='skyblue', fg='white', font=('Arial', 10), padx=10, pady=5,
                        command=lambda cat=category: show_search_window(cat, items_in_store))  # Pass items_in_store
        btn.grid(row=i, column=0, pady=5)

    quit_btn = tk.Button(category_frame, text="Quit", bg='red', fg='white', font=('Arial', 10), padx=10, pady=5,
                         command=root.quit)
    quit_btn.grid(row=len(categories)+1, column=0, pady=5)

    # Button to pay for selected items
    pay_btn = tk.Button(root, text="Pay", bg='green', fg='white', font=('Arial', 10), padx=10, pady=5, command=pay)
    pay_btn.grid(row=1, column=0, pady=5)

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
