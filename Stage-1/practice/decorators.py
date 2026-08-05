import functools
import time 

def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwrgs):
        start = time.time()
        result = func(*args,**kwrgs)
        end = time.time()
        print(f"Time took {(end-start):.8f}")
        return result
    return wrapper

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args,**kwrgs):
        for i in args:
            if i<= 0:
                raise ValueError("Arguments must be positive")
        return func(*args,**kwrgs)
    return wrapper

@validate_positive
@timer
def calculate_interest(principal : float, rate : float) -> float:
    result = principal * rate / 100
    return result

obj1 = calculate_interest(1000.0,5.0)

print(obj1)

try:
    obj2 = calculate_interest(-500,5)
    print(obj2)
except ValueError as e:
    print(e)


@timer
def add(a:int , b:int):
    return a+b
obj = add(5,10)
print(obj)
