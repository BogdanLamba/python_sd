
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
import decimal

# 1. Basic Dataclass
@dataclass
class Point:
    x: float
    y: float


# 2. Dataclass with Default Values
@dataclass
class Configuration:
    host: str
    port: int
    debug: bool = False


# 3. Immutable Dataclass
@dataclass(frozen=True)
class Settings:
    api_key: str
    timeout: int = 30


# 4. Dataclass with Type Hints
@dataclass
class Student:
    name: str
    age: int
    grades: List[float]
    email: Optional[str] = None


# 5. Dataclass with Post-Init Processing
@dataclass
class Circle:
    radius: float
    area: float = 0.0

    def __post_init__(self):
        self.area = 3.14 * self.radius ** 2


# 6. Inheritance with Dataclasses
@dataclass
class Animal:
    name: str
    species: str


@dataclass
class Dog(Animal):
    breed: str


# 7. Dataclass with Field Options
@dataclass
class ShoppingCart:
    items: List[str] = field(default_factory=list)
    total: float = field(init=False, default=0.0)


# 8. Dataclass with Comparison Methods
@dataclass(order=True)
class Item:
    name: str
    price: float


# 9. Real-World Example: Order System
@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: decimal.Decimal

    def get_total(self) -> decimal.Decimal:
        return self.price * self.quantity


@dataclass
class Order:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    order_date: datetime = field(default_factory=datetime.now)
    shipping_address: Optional[str] = None

    def get_total_amount(self) -> decimal.Decimal:
        return sum(item.get_total() for item in self.items)


# Usage Examples
if __name__ == "__main__":
    # Basic Point
    p = Point(1.0, 2.0)
    print(f"Point: {p}")

    # Configuration
    config = Configuration("localhost", 8080)
    print(f"Config: {config}")

    # Settings (Immutable)
    settings = Settings("abc123")
    print(f"Settings: {settings}")
    # This would raise an error: settings.api_key = "xyz"  # FrozenInstanceError

    # Student with grades
    student = Student("Alice", 20, [95.5, 87.0, 92.5])
    print(f"Student: {student}")

    # Circle with calculated area
    circle = Circle(5.0)
    print(f"Circle area: {circle.area}")

    # Dog inheriting from Animal
    dog = Dog("Rex", "Canis", "German Shepherd")
    print(f"Dog: {dog}")

    # Shopping cart with default empty list
    cart = ShoppingCart()
    cart.items.append("Book")
    print(f"Cart: {cart}")

    # Ordered items
    item1 = Item("A", 10.0)
    item2 = Item("B", 5.0)
    print(f"Is item1 > item2? {item1 > item2}")

    # Order system
    items = [
        OrderItem("LAPTOP", 1, decimal.Decimal("999.99")),
        OrderItem("MOUSE", 2, decimal.Decimal("29.99"))
    ]
    order = Order("ORD123", "CUST456", items)
    print(f"Order total: ${order.get_total_amount()}")