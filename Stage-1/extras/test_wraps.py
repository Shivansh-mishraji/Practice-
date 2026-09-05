from functools import wraps

# ==========================================
# TEST 1: Decorator WITHOUT @wraps
# ==========================================
def bad_decorator(func):
    def wrapper():
        return func()
    return wrapper

@bad_decorator
def login_user():
    """This function logs in the user."""
    return "User Logged In"

print("--- WITHOUT @wraps ---")
print("What is the function name?", login_user.__name__)
print("What is the documentation?", login_user.__doc__)

# ==========================================
# TEST 2: Decorator WITH @wraps
# ==========================================
def good_decorator(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper

@good_decorator
def logout_user():
    """This function logs out the user."""
    return "User Logged Out"

print("\n--- WITH @wraps ---")
print("What is the function name?", logout_user.__name__)
print("What is the documentation?", logout_user.__doc__)
