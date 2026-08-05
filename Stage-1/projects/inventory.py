"""
Inventory Management System — Sprint 1, Day 1-2
Production-quality Python: classes, type hints, @property, exceptions, magic methods.
"""


class Product:
    """
    Represents a single product in the inventory.
    Uses @property for validated price access and a read-only stock check.
    """

    def __init__(self, name: str, price: float, quantity: int, category: str) -> None:
        # Store name and category directly (no validation needed)
        self.name = name
        self.category = category
        self.quantity = quantity
        # Use the setter from the start — validation happens inside it
        self.price = price  # ← this calls @price.setter below

    # --- @property pattern ---
    # Step 1: GETTER — called when you READ p.price
    @property
    def price(self) -> float:
        return self._price  # stored privately as _price

    # Step 2: SETTER — called when you WRITE p.price = value
    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Price must be > 0, got {value}")
        self._price = value  # only stored if valid

    # Step 3: READ-ONLY property (no setter = assignment raises AttributeError)
    @property
    def is_in_stock(self) -> bool:
        """True if at least 1 unit is available."""
        return self.quantity > 0  # cleaner than 'True if x else False'

    def __repr__(self) -> str:
        stock_status = "In Stock" if self.is_in_stock else "Out of Stock"
        return f"Product({self.name!r}, price={self.price:.2f}, qty={self.quantity}, [{stock_status}])"


class Inventory:
    # FIX 4: Move the list INSIDE __init__ — instance variable, not class variable.
    # Class variables are shared across ALL instances. That's the bug.
    def __init__(self) -> None:
        self._products: list[Product] = []  # private, per-instance

    # FIX 5: Add 'self' OR use @staticmethod. Since we need instance data, use self.
    def add_product(self, product: Product) -> None:
        """Add a product. Raises ValueError if a product with same name exists."""
        # FIX 6: Check by NAME, not by object identity.
        # product in self._products would use __eq__ (name + price + qty + cat).
        # But checking by name is clearer intent.
        if any(p.name == product.name for p in self._products):
            raise ValueError(f"Product '{product.name}' already exists in inventory.")
        self._products.append(product)

    def remove_product(self, name: str) -> None:
        """Remove a product by name. Raises ValueError if not found."""
        original_count = len(self._products)
        self._products = [p for p in self._products if p.name != name]
        # FIX 7: Raise if nothing was removed (product didn't exist).
        if len(self._products) == original_count:
            raise ValueError(f"Product '{name}' not found in inventory.")

    def get_by_category(self, category: str) -> list[Product]:
        """Return all products in a given category."""
        return [p for p in self._products if p.category == category]

    def total_value(self) -> float:
        """Return total inventory value (price * quantity for all products)."""
        return sum(p.price * p.quantity for p in self._products)

    # FIX 8: __repr__ MUST return a string. Always.
    def __repr__(self) -> str:
        return f"Inventory({len(self._products)} products)"

    # FIX 9: __len__ needs self.
    def __len__(self) -> int:
        return len(self._products)



def run_cli() -> None:
    """Run the interactive inventory CLI."""
    # FIX 10: Create ONE instance. Don't use class as a static namespace.
    inventory = Inventory()

    while True:
        print("""
=== Inventory Manager ===
1. Add Product
2. Remove Product
3. Filter by Category
4. Total Value
5. Show All Products
6. Exit
========================""")

        try:
            choice = int(input("Choice: "))

            if choice == 1:
                name = input("Name: ").strip()
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                category = input("Category: ").strip()
                product = Product(name=name, price=price, quantity=quantity, category=category)
                inventory.add_product(product)
                print(f"✅ Added: {product}")

            elif choice == 2:
                name = input("Product name to remove: ").strip()
                inventory.remove_product(name)
                print(f"✅ Removed '{name}'.")

            elif choice == 3:
                category = input("Category: ").strip()
                results = inventory.get_by_category(category)
                if results:
                    for p in results:
                        print(f"  → {p}")
                else:
                    print("No products found in that category.")

            elif choice == 4:
                print(f"Total inventory value: ₹{inventory.total_value():.2f}")

            elif choice == 5:
                if not inventory:  # uses __len__ → len(inventory) == 0
                    print("Inventory is empty.")
                else:
                    print(f"\n{inventory}")  # uses __repr__
                    for p in inventory._products:
                        print(f"  → {p}")

            elif choice == 6:
                print("Goodbye.")
                break

            else:
                print("Invalid choice. Enter 1–6.")

        except ValueError as e:
            # Specific: catches bad input AND our custom validation errors
            print(f"❌ Error: {e}")
        # FIX 11: No bare 'except Exception' swallowing unknown crashes.
        # Let real bugs crash loudly — that's how you find them.


if __name__ == "__main__":
    run_cli()