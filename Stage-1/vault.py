import functools
import time
from dataclasses import dataclass


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executing {func.__name__} finished in {end - start:.6f} seconds")
        return result
    return wrapper


def validate_non_empty(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and not arg.strip():
                raise ValueError("String argument cannot be empty")
        return func(*args, **kwargs)
    return wrapper


@dataclass
class Transaction:
    tx_id: str
    amount: float
    tx_type: str = "DEPOSIT"

    def __repr__(self) -> str:
        return f"Transaction(id={self.tx_id!r}, type={self.tx_type!r}, amount=Rs.{self.amount:.2f})"


class Vault:
    @validate_non_empty
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = initial_balance
        self._history: list[Transaction] = []

    @property
    def balance(self) -> float:
        return self._balance

    @log_execution
    def process_transaction(self, tx: Transaction) -> float:
        if tx.tx_type == "DEPOSIT":
            self._balance += tx.amount
        elif tx.tx_type == "WITHDRAWAL":
            if tx.amount > self._balance:
                raise ValueError("Insufficient Vault Balance")
            self._balance -= tx.amount
        self._history.append(tx)
        return self._balance

    def __len__(self) -> int:
        return len(self._history)

    def __repr__(self) -> str:
        return f"Vault(owner={self.owner!r}, balance=Rs.{self.balance:.2f}, transactions={len(self)})"


if __name__ == "__main__":
    vault = Vault("Shivansh", 1000.0)
    tx1 = Transaction("TX101", 500.0, "DEPOSIT")
    tx2 = Transaction("TX102", 200.0, "WITHDRAWAL")
    vault.process_transaction(tx1)
    vault.process_transaction(tx2)
    print(vault)
