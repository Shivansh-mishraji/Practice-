from typing import Optional , Callable , Union

# 1. User profile builder
# name is required, bio is optional (might be None)
# Return a dict with both fields
def build_profile(name: str, bio: Optional[str] = None) -> dict[str, Optional[str]]:
    return {"name": name, "bio": bio}
# 2. Flexible formatter
# value could be str, int, or float — convert ALL to string
# If int/float, format with 2 decimal places

def format_value(value: Union[str,float,int]) -> str:
    if isinstance(value, float) or isinstance(value, int):
        return f"{value:.2f}"
    return str(value)

# 3. Apply a math operation
# op is a FUNCTION that takes 2 ints and returns an int
# Apply it to a and b
def apply_operation(op: Callable[[int,int],int], a: int, b: int) -> int:
    return op(a,b)
def op(a: int,b:int) -> int:
    return (a+b)**2

    
if __name__ == "__main__":
    # Test 1: Optional
    assert build_profile("Shivansh", "Backend Dev") == {"name": "Shivansh", "bio": "Backend Dev"}
    assert build_profile("Shivansh", None) == {"name": "Shivansh", "bio": None}
    assert build_profile("Shivansh") == {"name": "Shivansh", "bio": None}

    # Test 2: Union
    assert format_value("hello") == "hello"
    assert format_value(42) == "42.00"
    assert format_value(3.14) == "3.14"

    # Test 3: Callable
    assert apply_operation(lambda a, b: a + b, 3, 4) == 7
    assert apply_operation(lambda a, b: a * b, 3, 4) == 12

    print("All tests passed!")
