from dataclasses import dataclass
@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    @property
    def balance(self)->float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Balance cannot be negative, got {value}")
        self._balance = value   
    
    def deposit(self,amount: float) -> None:
        if amount>0:
            self.balance += amount
        else:
            raise ValueError("Invalid amount")
    
    def withdraw(self,amount: float) -> None:
        if amount <= 0:
            raise ValueError("invalid withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
    def __repr__(self) -> str :
        return f"BankAccount(owner='{self.owner}',balance={self.balance})"

    @property
    def is_empty(self) ->bool:
        return self.balance == 0
    
