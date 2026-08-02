class Product:
    def __init__(self , name: str, price: float,discount :float) -> None:
        self.name = name
        self.price = price
        self.discount = discount
    @property
    def discount(self) -> float:
        return self._discount
    
    @discount.setter
    def discount(self,value:float) -> None:
        if value < 0.0 or value > 50.0:
            raise ValueError("discount must be between 0.0 and 50.0") 
        self._discount = value

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self,value : float) -> None:
        if value <0:
            raise ValueError("price must be >0")
        self._price = value
        
    @property
    def final_price(self) -> float:
        return self._price * (1 - self._discount /100)

    def __repr__(self) -> str:
        return f"Product(name = {self.name},price = {self.price:.2f},discount = {self.discount}%, final_price ={self.final_price:.2f})"


if __name__ == "__main__":
    p1 = Product("Laptop", 1200.0, 10.0)
    print(f"Initial Final Price: {p1.final_price}")  # 1080.0

    # Test invalid price
    try:
        p1.price = -50
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # Test invalid discount
    try:
        p1.discount = 75
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # Test setting read-only property
    try:
        p1.final_price = 500
    except AttributeError as e:
        print(f"Caught expected error: {e}")

    