-----------Introduction-----:
This Python application is designed to simulate a simple supermarket shopping experience using a graphical user interface (GUI) built with the Tkinter library.

-----------Features------------:
Category Selection: Users can choose from different categories such as Vegetables, Fruits, Dairy Products, and Meat and Poultry.
Item Search: Within each category, users can search for specific items using a search functionality.
Item Display: The application displays the name, quantity, and price of items matching the search query.
Item Purchase: Users can select and buy items, and the quantity available decreases accordingly.
Payment: Once users are done shopping, they can proceed to pay for their selected items using a payment form.
Validation: The application performs validation checks on card number, security code, and expiry date during payment processing.
Out of Stock Handling: If an item is out of stock, a message is displayed, and the user cannot buy it.
--------Usage--------------:
Running the Application: Execute the script main.py to launch the application.
Category Selection: Click on the desired category button to browse items within that category.
Item Search: Enter a query in the search window to find specific items within the selected category.
Item Purchase: Click on the "Buy" button next to an item to add it to the shopping cart.
Payment: After selecting items, click on the "Pay" button to proceed to the payment window.
Payment Processing: Enter valid card details (16-digit card number, 3-digit security code, and MM/YY expiry date) and click "Confirm Payment" to complete the transaction.
Exiting the Application: Click on the "Quit" button in the category selection window to exit the application.
-----------Dependencies----------:
Python 3.x
Tkinter library (usually included with Python installation)
File Structure:
main.py: Main script to run the application.
items_data.txt: Text file containing item data (category, name, quantity, price).
README.md: Documentation file explaining the application's features and usage.
