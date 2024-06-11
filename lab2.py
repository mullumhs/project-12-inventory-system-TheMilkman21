"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item




# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.
class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                return False
        item = Item(name, price, quantity)
        self.items.append(item)
        return True
        
    def remove_item(self, name):
        for i, existing_item in enumerate(self.items):
            if existing_item.get_name() == name:
                del self.items[i]
                print(f"{name} has been removed")
                return True
        return False
    
    def update_item(self, name, new_price, new_quantity):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                existing_item.set_price(new_price)
                existing_item.set_quantity(new_quantity) 
                print(f"{name} price updated to {new_price}")
                print(f"{name} quantity to {new_quantity}")
                return True
        return False
            
    def display_item(self):
        for item in self.items:
            print(f"Item name: {item.get_name()}, price: ${item.get_price()}, quantity: {item.get_quantity()}")
            
    def find_item(self, name):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                return existing_item
        return None

    
# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

weapons = ItemManager()

weapons.add_item("sword", 5, 1)
weapons.add_item("bat", 2, 1)
weapons.add_item("gun", 20, 1)
weapons.display_item()
weapons.update_item("sword", 15, 3)
weapons.remove_item("bat")
weapons.display_item()

