from dataclasses import dataclass, field
from typing import List

@dataclass
class CartItem:
    item_name: str
    item_price: float
    item_quantity: int
    
    def get_subtotal(self) -> float:
        return self.item_price * self.item_quantity

@dataclass
class Cart:
    items: List[CartItem] = field(default_factory=list)
    
    def add_item(self, item_name: str, item_price: float, item_quantity: int) -> None:
        cart_item = CartItem(item_name, item_price, item_quantity)
        self.items.append(cart_item)
    
    def clear_duplicated_items(self) -> None:
        # Create a dictionary to store unique items
        unique_items = {}
        for item in self.items:
            key = (item.item_name, item.item_price)  # Unique key based on name and price
            if key in unique_items:
                # If item exists, add quantities
                unique_items[key].item_quantity += item.item_quantity
            else:
                unique_items[key] = item
        # Update items list with unique items
        self.items = list(unique_items.values())
    
    def get_total(self) -> float:
        return sum(item.get_subtotal() for item in self.items)
    
    def print_cart(self) -> None:
        print("Shopping Cart Contents:")
        print("-" * 50)
        for item in self.items:
            print(f"Item: {item.item_name}")
            print(f"Price: ${item.item_price:.2f}")
            print(f"Quantity: {item.item_quantity}")
            print(f"Subtotal: ${item.get_subtotal():.2f}")
            print("-" * 50)
        print(f"Total: ${self.get_total():.2f}")

def main():
    # Create a new cart
    cart = Cart()
    
    # Add items including duplicates
    cart.add_item("Book", 29.99, 2)
    cart.add_item("Pen", 4.99, 3)
    cart.add_item("Book", 29.99, 1)  # Duplicate item
    
    print("Before removing duplicates:")
    cart.print_cart()
    
    cart.clear_duplicated_items()
    
    print("\nAfter removing duplicates:")
    cart.print_cart()

if __name__ == "__main__":
    main()
