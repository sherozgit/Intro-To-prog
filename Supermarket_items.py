import tkinter as tk
from tkinter import messagebox
# Global variables to store the items selected by the user and their quantities
selected_items = []
item_counters = {}

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
            # Counter label for quantity
            counter_label = tk.Label(result_window, text="0")
            counter_label.grid(row=i, column=2)
            # Store the counter label in a dictionary with item name as key
            item_counters[item_name] = counter_label
    else:
        # Displaying a message if no items match the query
        tk.Label(result_window, text=f"No items matching '{query}' found in {category.capitalize()}.").grid(row=0, column=0)

# Function to handle buying items
def buy_item(name, details):
    available_quantity = details['quantity']
    if available_quantity > 0:
        selected_items.append((name, details))
        # Decrement the available quantity and update the counter label
        details['quantity'] -= 1
        item_counters[name].config(text=str(int(item_counters[name].cget("text")) + 1))
    else:
        # Display a message if the item is out of stock
        tk.messagebox.showinfo("Out of Stock", f"{name} is currently out of stock.")

# Function to handle paying for the selected items
def pay():
    total_amount = sum(item[1]['price'] for item in selected_items)

    # Create a new window for payment form
    payment_window = tk.Toplevel()
    payment_window.title("Payment")
    
    # Labels and entry widgets for card number and expiry date
    tk.Label(payment_window, text="Card Number:").grid(row=0, column=0, padx=10, pady=5)
    card_number_entry = tk.Entry(payment_window)
    card_number_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(payment_window, text="Expiry Date (MM/YY):").grid(row=1, column=0, padx=10, pady=5)
    expiry_date_entry = tk.Entry(payment_window)
    expiry_date_entry.grid(row=1, column=1, padx=10, pady=5)
    
    # Function to process payment
    def process_payment():
        card_number = card_number_entry.get()
        expiry_date = expiry_date_entry.get()
        # You can add further validation here if needed
        # For demonstration purposes, just show a message
        tk.messagebox.showinfo("Payment", f"Payment successful. Thank you for shopping! Total amount: ${total_amount:.2f}")
        # Close the payment window after successful payment
        payment_window.destroy()

    # Button to confirm payment
    confirm_btn = tk.Button(payment_window, text="Confirm Payment", command=process_payment)
    confirm_btn.grid(row=2, columnspan=2, padx=10, pady=10)
# Main function to create the main window and handle user interaction
def main():
    # Read item data from file
    items_in_store = read_item_data('items_data.txt')
    
    # Create main window
    root = tk.Tk()
    root.title("Supermarket")
    root.configure(bg='black')
    root.geometry("200x400")

    # Create category selection frame
    category_frame = tk.Frame(root, bg='lightgray',width=300)  # Specify background color for the frame
    category_frame.grid(row=0, column=0, padx=10, pady=10)

    # Label for category selection
    tk.Label(category_frame, text="Select a category:").grid(row=0, column=0, columnspan=2)

    # List of categories
    categories = ['Vegetables', 'Fruits', 'Dairy Products', 'Meat and Poultry']
    # Creating buttons for each category
    for i, category in enumerate(categories, start=1):
        btn = tk.Button(category_frame, text=category, bg='skyblue', fg='white', font=('Arial', 10), padx=20, pady=5,
                        command=lambda cat=category: show_search_window(cat, items_in_store))  # Pass items_in_store
        btn.grid(row=i, column=0, pady=10)

    quit_btn = tk.Button(category_frame, text="Quit", bg='red', fg='white', font=('Arial', 13), padx=20, pady=5,
                         command=root.quit)
    quit_btn.grid(row=len(categories)+1, column=0, pady=10)

    # Button to pay for selected items
    pay_btn = tk.Button(root, text="Pay", bg='green', fg='white', font=('Arial', 15), padx=10, pady=5, command=pay)
    pay_btn.grid(row=1, column=0, pady=10)

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
    search_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Entry point of the program
if __name__ == "__main__":
    main()
