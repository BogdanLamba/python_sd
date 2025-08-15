from dataclasses import dataclass, field


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int

    def get_subtotal(self) -> float:
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    items: list[CartItem] = field(default_factory=list)

    def add_to_cart(self, item_name: str, item_price: float, item_quantity: int) -> None:
        cart_item = CartItem(item_name, item_price, item_quantity)
        self.items.append(cart_item)

    def print_cart(self) -> None:
        for item in self.items:
            print("-" * 10)
            print(f"Item: {item.name}")
            print(f"Price: ${item.price:.2f}")
            print(f"Quantity: {item.quantity}")
            print(f"Subtotal: ${item.get_subtotal():.2f}")

    def sort_cart(self) -> None:
        self.items.sort(key=lambda item: item.name)
        print(self.items)
        for item in self.items:
            print(item.name)


def main():
    shopping_cart = ShoppingCart()
    shopping_cart.add_to_cart("Laptop", 999.99, 1)
    shopping_cart.add_to_cart("Disc", 229.99, 2)
    shopping_cart.add_to_cart("Mouse", 19.99, 2)
    shopping_cart.add_to_cart("Pad", 12.99, 1)

    shopping_cart.print_cart()

    shopping_cart.sort_cart()

if __name__ == "__main__":
    main()
