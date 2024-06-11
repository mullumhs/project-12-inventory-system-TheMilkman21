"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 3
-----------------------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a user interface for the Inventory Management System. This interface will
               allow users to interact with the InventoryManager to add, update, remove, and view
               items in the inventory using a command-line interface.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import necessary classes (Item class from lab1, InventoryManager class from lab2)
from lab1 import Item; from lab2 import ItemManager

# Step 2: Define an add_item function that prompts the user for item details and adds the item to the inventory
def add_item():
    name = input("enter name of item: ")
    price = float(input("enter price: "))
    quantity = int(input("enter quantity: "))
    item = Item(name, price, quantity)
    if ItemManager.add_item(item):
        print("added the item")
    else:
        print("cant add that")

# Step 3: Define an update_item function that prompts the user for item details and updates the item in the inventory
def update_item():
    name = print("enter item you want to update: ")
    price = print("Enter new price (leave blank to keep current): ")
    quantity = print("Enter new quantity (leave blank to keep current):")
    if price:
        price = float(price)
    else:
        price = None
        
    if quantity:
        quantity = int(quantity)
    else:
        quantity = None
        
    if ItemManager.update_item(name, price, quantity):
        print("Ticket updated successfully.")
    else:
        print("Ticket not found or no updates made.")

# Step 4: Define a remove_item function that prompts the user for an item name and removes the item from the inventory
def remove_item():
    name = input("enter item you want to remove: ")
    if ItemManager.remove_item(name):
        print("removed")
    else:
        print("item not found")
    

# Step 5: Define a display_inventory function that displays all items in the inventory
def display_items():
    print("Current items:")
    ItemManager.display_item()
    
def main():
    manager = ItemManager()
    actions = {
        '1': add_item,
        '2': update_item,
        '3': remove_item,
        '4': display_items
    }
def main():
    # Step 6: Initialise an instance of InventoryManager
    

    # Step 7: Use the actions dictionary to map user input to the corresponding functions
    actions = {}
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")
        
        if

        # Step 8: Implement the logic to call the appropriate function based on user input
        # Exit the loop if the user chooses 5, otherwise display an error message for invalid choices


        

if __name__ == "__main__":
    main()