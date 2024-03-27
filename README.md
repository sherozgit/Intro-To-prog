import tkinter as tk
#Function to read item data from a file and store it in a nested dictionary
def read_item_data(filename):
    items_data = {}
    with open(filename, 'r') as file:
        for line in file:
            #Spliting each of the file into category, name, quantity and price
            category, name, quantity, price = line.strip().split(',')
            #Creating a nested dictionary to store item details 
            item = {'name': name, 'quantity': int(quantity), 'price': float(price)}
            #Chech if the category exists in items_data
            if category in item_data:
                items_data[category][name] = item
            else:
                items_data[category] = {name:item}
    return items_data

def search_items(items_data, category,query):
    result_window = tk.Tk()
    result_window.title("Search Results")

    # List to store found items
    found_items = []
    # Iterating through items in the specified category
    for item in items_data.get(category, []):
        # Checking if the query string matches any part of the item name (case insensitive)
        if query.lower() in item['name'].lower():
            found_items.append(item)

    if found_items:
        # Displaying search results
        for i, item in enumerate(found_items):
            tk.Label(result_window, text=f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}").grid(row=i, column=0)
    else:
        # Displaying a message if no items match the query
        tk.Label(result_window, text=f"No items matching '{query}' found in {category.capitalize()}.").grid(row=0, column=0)
# Main function to create the main window and handle user interaction
def main():
    #Read item data from file     
    items_in_store = read_item_data('items_data.txt')
    #Create main window
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
        btn = tk.Button(category_frame, text=category, bg='skyblue', fg='white', font=('Arial', 10), padx=10, pady=5,
                        command=lambda cat=category: show_search_window(cat, items_in_store))  # Pass items_in_store
        btn.grid(row=i, column=0, pady=5)

    quit_btn = tk.Button(category_frame, text="Quit", bg='red', fg='white', font=('Arial', 10), padx=10, pady=5,
                         command=root.quit)
    quit_btn.grid(row=len(categories)+1, column=0, pady=5)

    root.mainloop()
# Function to create a search window for a specific category
def show_search_window(category, items_data):
    search_window = tk.Toplevel()
    search_window.title(f"Search {category.capitalize()}")

    tk.Label(search_window, text=f"What are you looking for in {category.capitalize()}?").grid(row=0, column=0)
    query_entry = tk.Entry(search_window)
    query_entry.grid(row=0, column=1)
    search_btn = tk.Button(search_window, text="Search", command=lambda: search_items(items_data, category.lower(), query_entry.get()))
    search_btn.grid(row=1, column=0, columnspan=2, pady=5)

    


# Entry point of the program
if __name__ == "__main__":
    main()
