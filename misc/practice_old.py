from dataclasses import dataclass, field

@dataclass
class CartItem:
    item_name: str
    item_quantity: int
    item_price: float

    def get_subtotal(self) -> float:
        return self.item_quantity * self.item_price


@dataclass
class ShoppingCart:
    items: list[CartItem] = field(default_factory=list)

    def add_to_cart(self, item_name: str, item_quantity: int, item_price: float) -> None:
        cart_item = CartItem(item_name, item_quantity, item_price)
        self.items.append(cart_item)

    def get_total_payment(self) -> float:
        return sum(item.get_subtotal() for item in self.items)

    def print_shopping_cart(self) -> None:
        for item in self.items:
            print(*[item.item_name, item.item_quantity, item.item_price])

    def clear_cart(self) -> None:
        """Șterge toate produsele din coș."""
        self.items.clear()

def main():
    shopping_cart = ShoppingCart()
    shopping_cart.add_to_cart("Laptop", 1, 999.99)
    shopping_cart.add_to_cart("Mouse", 2, 29.9)

    total = shopping_cart.get_total_payment()
    print(f"Total înainte: {total}")
    shopping_cart.print_shopping_cart()
    
    # Testează clear_cart()
    shopping_cart.clear_cart()
    print(f"\nDupă clear_cart():")
    print(f"Total după: {shopping_cart.get_total_payment()}")
    print(f"Număr items: {len(shopping_cart.items)}")


if __name__ == "__main__":
    main()
