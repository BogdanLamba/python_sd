def shopping(shopping_list):
    """
    Display and return a shopping list from a list of tuples.
    
    Args:
        shopping_list (list): List of tuples containing (item, quantity) pairs
    Returns:
        list: The shopping list as a list of tuples
    """
    print("\nYour shopping list:")
    for item, quantity in shopping_list:
        print(f"{item}: {quantity}")
    return shopping_list

def create_shopping_list(num_items):
    """
    Create a shopping list by getting user input.
    
    Args:
        num_items (int): Number of items to add to the list
    Returns:
        list: List of tuples containing items and their quantities
    """
    shopping_list = []
    
    for i in range(num_items):
        item = input("Enter the item: ").strip()
        while True:
            try:
                quantity = int(input("Enter the quantity: "))
                if quantity > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
        
        shopping_list.append((item, quantity))
    return shopping_list

def remove_from_shopping_list(shopping_list, item_name):
    """
    Remove an item from the shopping list by its name.

    Args:
        shopping_list (list): List of tuples containing (item, quantity) pairs
        item_name (str): Name of the item to remove
    Returns:
        list: The modified shopping list with the item removed if found
    """
    return [(item, quantity) for item, quantity in shopping_list if item.lower() != item_name.lower()]


# Main program
num_items = 3  # You can change this number to allow more or fewer items
my_shopping_list = create_shopping_list(num_items)
shopping(my_shopping_list)