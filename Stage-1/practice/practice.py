# class OutOfStockError(Exception):
#     def __init__(self,item_name: str ):
#         self.item_name = item_name
#     def __str__(self):
#         return f"Item '{self.item_name}' is completely out of stock!"
# raise OutOfStockError("iPhone15")
"""
Write a class BankAccount with _balance private,
 a balance getter,
 a deposit setter that raises ValueError if amount ≤ 0,
 and a withdraw method."

"""
class BankAccount :
    def __init__(self, balance :int) -> None :
        self.balance = balance
    @property
    def balance(self) -> int:
        return self._balance
    @balance.setter
    def balance(self,amount :int) -> None:
        if amount < 0:
            raise ValueError(f"Amount caannot be less than 0")
        self._balance = amount
    def deposit(self,amount : int) -> None :
        if amount < 0:
            raise ValueError(f"Amount cannot be less than 0, got {amount}")
        self._balance += amount
    def withdraw(self,amount : int) -> None :
        if amount > self._balance :
            raise ValueError(f"Insufficient Balance , Present Balance ={self._balance}")
        self._balance -= amount
if __name__ == "__main__":
    b = BankAccount(500)
    b.deposit(200)
    assert b.balance == 700
    b.withdraw(300)
    assert b.balance == 400
    print("All tests passed!")
