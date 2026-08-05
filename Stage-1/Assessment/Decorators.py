# ========================================
# ASSESSMENT: Decorators + Closures
# Status: PASSED with 2 improvements
# ========================================

# MISTAKE 1: wrapper() doesn't accept *args, **kwargs
# This means @logger breaks for ANY function with parameters.
# FIX: Always use *args, **kwargs in wrapper.

# MISTAKE 2: Missing @wraps(func) from functools
# Without it, the decorated function loses its __name__ and __doc__.
# FIX: Add `from functools import wraps` and `@wraps(func)`.

# LESSON: Every decorator you write in production MUST have these two things.

from functools import wraps


# --- Decorator ---
def logger(func):
    @wraps(func)  # FIX: preserves function name and docstring
    def wrapper(*args, **kwargs):  # FIX: was `wrapper()` with no params
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result  # FIX: return the result so decorated functions work properly
    return wrapper


@logger
def greet(name: str) -> str:
    """Greets a person by name."""
    return f"Hello, {name}!"


# --- Closure: Variable Capture ---
# The inner function "remembers" x from outer's scope even after outer() finishes.
def outer():
    x = 5
    def inner():
        print(x)
    return inner


# --- Closure: Counter with nonlocal ---
# `nonlocal` lets inner modify outer's variable (not just read it).
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print(count)
    return increment


if __name__ == "__main__":
    # Test decorator with arguments (would fail with old code!)
    result = greet("Shivansh")
    print(result)
    # Verify @wraps preserved the function name
    assert greet.__name__ == "greet", "BUG: @wraps missing!"
    print("-" * 30)

    # Test closure
    f = outer()
    f()
    print("-" * 30)

    # Test counter
    c = counter()
    c()
    c()

    print("All tests passed!")