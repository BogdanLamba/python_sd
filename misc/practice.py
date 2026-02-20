"""
Shopping Cart Management System

This module provides a production-ready implementation of a shopping cart
with full CRUD operations, validation, and error handling.
"""

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MIN_QUANTITY = 1
MIN_PRICE = 0.01
MAX_PRICE = 999999.99
MAX_DISCOUNT = 100.0
MIN_DISCOUNT = 0.0


class ShoppingCartError(Exception):
    """Base exception for shopping cart errors."""
    pass


class InvalidQuantityError(ShoppingCartError):
    """Raised when quantity is invalid."""
    pass


class InvalidPriceError(ShoppingCartError):
    """Raised when price is invalid."""
    pass


class ItemNotFoundError(ShoppingCartError):
    """Raised when item is not found in cart."""
    pass


class InvalidDiscountError(ShoppingCartError):
    """Raised when discount percentage is invalid."""
    pass


@dataclass
class CartItem:
    """
    Represents a single item in the shopping cart.
    
    Attributes:
        item_name: Name of the product
        item_quantity: Quantity of the product (must be >= 1)
        item_price: Price per unit (must be > 0)
    """
    item_name: str
    item_quantity: int
    item_price: float

    def __post_init__(self) -> None:
        """Validate item attributes after initialization."""
        self._validate()

    def _validate(self) -> None:
        """Validate item attributes."""
        if not self.item_name or not self.item_name.strip():
            raise ValueError("Item name cannot be empty")

        if self.item_quantity < MIN_QUANTITY:
            raise InvalidQuantityError(
                f"Quantity must be at least {MIN_QUANTITY}, got {self.item_quantity}"
            )

        if self.item_price < MIN_PRICE or self.item_price > MAX_PRICE:
            raise InvalidPriceError(
                f"Price must be between {MIN_PRICE} and {MAX_PRICE}, got {self.item_price}"
            )

    def get_subtotal(self) -> float:
        """
        Calculate the subtotal for this item.
        
        Returns:
            The subtotal (quantity * price)
        """
        return round(self.item_quantity * self.item_price, 2)

    def __str__(self) -> str:
        """String representation of the cart item."""
        return f"{self.item_name} x{self.item_quantity} @ ${self.item_price:.2f} = ${self.get_subtotal():.2f}"


@dataclass
class ShoppingCart:
    """
    Manages a shopping cart with full CRUD operations.
    
    Attributes:
        items: List of CartItem objects in the cart
    """
    items: list[CartItem] = field(default_factory=list)

    def add_to_cart(self, item_name: str, item_quantity: int, item_price: float) -> None:
        """
        Add a new item to the cart.
        
        Args:
            item_name: Name of the product
            item_quantity: Quantity to add
            item_price: Price per unit
            
        Raises:
            InvalidQuantityError: If quantity is invalid
            InvalidPriceError: If price is invalid
            ValueError: If item name is empty
        """
        try:
            cart_item = CartItem(item_name, item_quantity, item_price)
            self.items.append(cart_item)
            logger.info(f"Added to cart: {cart_item}")
        except (InvalidQuantityError, InvalidPriceError, ValueError) as e:
            logger.error(f"Failed to add item '{item_name}': {e}")
            raise

    def remove_from_cart(self, item_name: str) -> bool:
        """
        Remove an item from the cart by name.
        
        Args:
            item_name: Name of the product to remove
            
        Returns:
            True if item was found and removed, False otherwise
        """
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                self.items.remove(item)
                logger.info(f"Removed from cart: {item_name}")
                return True

        logger.warning(f"Item not found for removal: {item_name}")
        return False

    def update_quantity(self, item_name: str, new_quantity: int) -> bool:
        """
        Update the quantity of an existing item.
        
        Args:
            item_name: Name of the product
            new_quantity: New quantity value
            
        Returns:
            True if item was found and updated, False otherwise
            
        Raises:
            InvalidQuantityError: If new quantity is invalid
        """
        if new_quantity < MIN_QUANTITY:
            raise InvalidQuantityError(
                f"Quantity must be at least {MIN_QUANTITY}, got {new_quantity}"
            )

        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                old_quantity = item.item_quantity
                item.item_quantity = new_quantity
                logger.info(f"Updated quantity for '{item_name}': {old_quantity} -> {new_quantity}")
                return True

        logger.warning(f"Item not found for quantity update: {item_name}")
        return False

    def get_item_count(self) -> int:
        """
        Get the total number of items in the cart.
        
        Returns:
            Sum of all item quantities
        """
        return sum(item.item_quantity for item in self.items)

    def get_total_payment(self) -> float:
        """
        Calculate the total payment for all items in the cart.
        
        Returns:
            Total price of all items
        """
        return round(sum(item.get_subtotal() for item in self.items), 2)

    def apply_discount(self, discount_percent: float) -> float:
        """
        Calculate total after applying a percentage discount.
        
        Args:
            discount_percent: Discount percentage (0-100)
            
        Returns:
            Total after discount
            
        Raises:
            InvalidDiscountError: If discount is invalid
        """
        if not MIN_DISCOUNT <= discount_percent <= MAX_DISCOUNT:
            raise InvalidDiscountError(
                f"Discount must be between {MIN_DISCOUNT}% and {MAX_DISCOUNT}%, got {discount_percent}%"
            )

        total = self.get_total_payment()
        discounted_total = round(total * (1 - discount_percent / 100), 2)
        logger.info(f"Applied {discount_percent}% discount: ${total:.2f} -> ${discounted_total:.2f}")
        return discounted_total

    def find_item(self, item_name: str) -> Optional[CartItem]:
        """
        Find an item in the cart by name.
        
        Args:
            item_name: Name of the product to find
            
        Returns:
            CartItem if found, None otherwise
        """
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                return item
        return None

    def is_empty(self) -> bool:
        """
        Check if the cart is empty.
        
        Returns:
            True if cart has no items, False otherwise
        """
        return len(self.items) == 0

    def clear_cart(self) -> None:
        """
        Remove all items from the cart.
        """
        item_count = len(self.items)
        self.items.clear()
        logger.info(f"Cart cleared. Removed {item_count} items")

    def print_shopping_cart(self) -> None:
        """
        Print a formatted summary of the shopping cart.
        """
        if self.is_empty():
            print("\n🛒 Shopping Cart is empty")
            return

        print("\n" + "=" * 60)
        print("🛒 SHOPPING CART")
        print("=" * 60)

        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item}")

        print("-" * 60)
        print(f"Total Items: {self.get_item_count()}")
        print(f"Total Price: ${self.get_total_payment():.2f}")
        print("=" * 60)

    def __len__(self) -> int:
        """Return the number of unique items in the cart."""
        return len(self.items)

    def __str__(self) -> str:
        """String representation of the shopping cart."""
        return f"ShoppingCart(items={len(self.items)}, total=${self.get_total_payment():.2f})"


def main() -> None:
    """
    Demonstrate shopping cart functionality with comprehensive examples.
    """
    print("=" * 60)
    print("SHOPPING CART MANAGEMENT SYSTEM - DEMO")
    print("=" * 60)

    # Initialize cart
    cart = ShoppingCart()

    # Test 1: Add items
    print("\n📦 Test 1: Adding items to cart")
    try:
        cart.add_to_cart("Laptop", 1, 999.99)
        cart.add_to_cart("Mouse", 2, 29.99)
        cart.add_to_cart("Keyboard", 1, 79.99)
        cart.print_shopping_cart()
    except ShoppingCartError as e:
        print(f"Error: {e}")

    # Test 2: Update quantity
    print("\n🔄 Test 2: Updating quantity")
    if cart.update_quantity("Mouse", 3):
        print("✓ Updated Mouse quantity to 3")
        cart.print_shopping_cart()

    # Test 3: Apply discount
    print("\n💰 Test 3: Applying discount")
    try:
        original_total = cart.get_total_payment()
        discounted_total = cart.apply_discount(10)
        print(f"Original Total: ${original_total:.2f}")
        print(f"After 10% discount: ${discounted_total:.2f}")
        print(f"You saved: ${original_total - discounted_total:.2f}")
    except InvalidDiscountError as e:
        print(f"Error: {e}")

    # Test 4: Find item
    print("\n🔍 Test 4: Finding item")
    found_item = cart.find_item("Laptop")
    if found_item:
        print(f"✓ Found: {found_item}")

    # Test 5: Remove item
    print("\n🗑️  Test 5: Removing item")
    if cart.remove_from_cart("Keyboard"):
        print("✓ Removed Keyboard")
        cart.print_shopping_cart()

    # Test 6: Item count
    print(f"\n📊 Test 6: Cart statistics")
    print(f"Unique items: {len(cart)}")
    print(f"Total items: {cart.get_item_count()}")
    print(f"Cart empty: {cart.is_empty()}")

    # Test 7: Clear cart
    print("\n🧹 Test 7: Clearing cart")
    cart.clear_cart()
    cart.print_shopping_cart()
    print(f"Cart empty: {cart.is_empty()}")

    # Test 8: Error handling
    print("\n⚠️  Test 8: Error handling examples")
    try:
        cart.add_to_cart("Invalid", -1, 10.0)
    except InvalidQuantityError as e:
        print(f"✓ Caught expected error: {e}")

    try:
        cart.add_to_cart("Invalid", 1, -10.0)
    except InvalidPriceError as e:
        print(f"✓ Caught expected error: {e}")

    try:
        cart.apply_discount(150)
    except InvalidDiscountError as e:
        print(f"✓ Caught expected error: {e}")

    print("\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
