# ========================================
# ASSESSMENT: @property — Getter, Setter, Validation
# Status: PASSED with 1 minor fix
# ========================================

# MISTAKE MADE: __init__ return type was `-> int` instead of `-> None`
# FIX: __init__ always returns None — it's a constructor, not a calculator.
# LESSON: Type hints must be accurate. `-> int` on __init__ is misleading.

# NOTE: Combining @dataclass with @property is an advanced pattern.
# @dataclass generates __init__ that routes through the setter automatically.

from dataclasses import dataclass


@dataclass
class Wallet:
    balance: int

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f"Balance cannot be Negative, got {amount}")
        self._balance = amount


if __name__ == "__main__":
    # Test 1: Valid wallet
    w1 = Wallet(500)
    print(f"Wallet balance: {w1.balance}")
    assert w1.balance == 500

    # Test 2: Negative balance should raise ValueError
    try:
        w2 = Wallet(-500)
        print("BUG: Should have raised ValueError!")
    except ValueError as e:
        print(f"Correctly caught: {e}")

    print("All tests passed!")
