print("---------------MY FIRST APPROACH----------------")

cart = []
cart.append({"item": "Laptop", "price": 999.99, "quantity": 1})
cart.append({"item": "Mouse", "price": 19.99, "quantity": 2})

def calculate(cart):
        print(sum(item["price"] * item["quantity"] for item in cart))

print(f"OLD WAY - > Total: ${calculate(cart)}")



print("---------------version of the above refactored----------------")
from dataclasses import dataclass
from typing import List


@dataclass
class CartItem:
    item: str
    price: float
    quantity: int

    def get_subtotal(self) -> float:
        return self.price * self.quantity


INITIAL_CART_ITEMS = [
    CartItem(item="Laptop", price=999.99, quantity=1),
    CartItem(item="Mouse", price=19.99, quantity=2)
]


def calculate_total(cart: List[CartItem]) -> None:
    total = sum(item.get_subtotal() for item in cart)
    print(total)


# Usage
cart = INITIAL_CART_ITEMS
calculate_total(cart)


print("--------------version of the above in a real world scenario---------------")
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: float

    def get_total(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    order_date: datetime = field(default_factory=datetime.now)
    shipping_address: Optional[str] = None

    def get_total_amount(self) -> float:
        return sum(item.get_total() for item in self.items)


# Usage
items = [
    OrderItem("LAPTOP", 1, 999.99),
    OrderItem("MOUSE", 2, 29.99)
]
order = Order("ORD123", "CUST456", items)
print(order.get_total_amount())  # 1059.97