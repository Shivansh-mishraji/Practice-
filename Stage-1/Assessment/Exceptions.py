# ========================================
# ASSESSMENT: Exception Handling — try/except/finally + Custom Exceptions
# Status: PASSED with 2 fixes
# ========================================

# MISTAKE 1: __init__ return type was `-> int` instead of `-> None`
# FIX: Constructors always return None.

# MISTAKE 2: `raise InsufficientFundsError(100)` was outside any try/except
# so it always crashed the program with an unhandled exception.
# FIX: Wrap in try/except to demonstrate proper error handling.
# LESSON: In production, unhandled exceptions kill your API server.

# --- try/except/finally flow ---
# Demonstrates: A always prints, ValueError is caught (B prints), finally always runs (C prints)
try:
    print("A")
    raise ValueError("Error")
except ValueError:
    print("B")
finally:
    print("C")

print("-" * 30)


# --- Custom Exception ---
class InsufficientFundsError(Exception):
    def __init__(self, funds: int) -> None:  # FIX: was `-> int`
        self.funds = funds

    def __str__(self) -> str:
        return f"Insufficient Funds, Current Funds are {self.funds}"


if __name__ == "__main__":
    # FIX: raise inside try/except, not bare at module level
    try:
        raise InsufficientFundsError(100)
    except InsufficientFundsError as e:
        print(f"Correctly caught: {e}")

    print("All tests passed!")