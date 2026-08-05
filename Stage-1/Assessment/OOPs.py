# ========================================
# ASSESSMENT: OOP — Classes, __repr__, __len__
# Status: PASSED with 1 bug fix
# ========================================

# --- Employee Class ---
# MISTAKE MADE: annual_salary() used `self.salary *= 12` which MUTATES
# the original salary. Calling it twice would give salary * 144.
# FIX: Use `return self.salary * 12` — calculate, don't mutate.
# LESSON: Never modify state in a method that's supposed to just return a value.

class Employee:
    def __init__(self, name: str, salary: int, department: str) -> None:
        self.name = name
        self.salary = salary
        self.department = department

    def annual_salary(self) -> int:
        # FIX: was `self.salary *= 12` — that mutates the original
        return self.salary * 12

    def display(self) -> str:
        return f"Name : {self.name}\nDepartment : {self.department}\nAnnual Salary = {self.annual_salary()}"


# --- Book Class ---
# No mistakes here. __repr__ and __len__ done correctly.

class Book:
    def __init__(self, name: str, pages: int) -> None:
        self.name = name
        self.pages = pages

    def __repr__(self) -> str:
        return f"Book({self.name})"

    def __len__(self) -> int:
        return self.pages


if __name__ == "__main__":
    e1 = Employee("Shivansh", 50000, "AI")
    print(e1.display())
    # Verify annual_salary doesn't mutate — call twice, should be same
    assert e1.annual_salary() == 600000
    assert e1.annual_salary() == 600000  # would fail with old code!
    print("-" * 30)
    book = Book("Python", 350)
    print(book)
    print(len(book))
    print("All tests passed!")
