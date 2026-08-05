# Stage 1 — Python Core Foundations

> **Status:** ✅ COMPLETED
> **Duration:** Week 1–2 (Aug 2–5, 2026)
> **Goal:** Master Python core patterns used in backend engineering

---

## What Was Learned

| Concept | File | Key Pattern |
|:---|:---|:---|
| OOP + `__repr__` + `__len__` | `inventory.py`, `Assessment/OOPs.py` | Class design, dunder methods |
| `@property` getter/setter | `bank.py`, `catalog.py`, `practice.py` | Private state, validation |
| Exception handling | `vault.py`, `Assessment/Exceptions.py` | `raise ValueError`, custom exceptions |
| Decorators + closures | `decorators.py`, `Assessment/Decorators.py` | `@wraps`, `*args/**kwargs`, closures |
| Generators + `yield` | `generator.py` | Lazy evaluation, generator chaining |
| DSA fundamentals | `DSA/two-sum.py` | HashMap O(n) pattern |

---

## Mistakes Made & Lessons Learned

| Mistake | Lesson |
|:---|:---|
| `self.salary *= 12` in a getter method | Never mutate state in methods that calculate values |
| `__init__ -> int` return type | Constructors always return `-> None` |
| `"ERROR" or "CRITICAL" not in log` | Python evaluates `or` before `not in` — use explicit `in` checks |
| Setter named `deposit` with `@balance.setter` | Setter method name MUST match the property name |
| `pass` before `yield` thinking it would skip | `pass` does nothing — use `continue` to skip iterations |
| `log_stream.split()` on a generator | Generators are iterable directly — no `.split()` needed |
| Catching exceptions inside setters | Let exceptions propagate up — callers handle them |

---

## File Structure

```
Stage-1/
├── Assessment/         # Self-assessment files with review comments
│   ├── Decorators.py
│   ├── Exceptions.py
│   ├── OOPs.py
│   └── Properties.py
├── DSA/                # Daily DSA practice
│   └── two-sum.py
├── bank.py             # BankAccount with @property validation
├── catalog.py          # Smart Product Catalog
├── decorators.py       # Custom timing and validation decorators
├── generator.py        # Lazy Log Stream Pipeline (3 chained generators)
├── interview_drills.py # Interview micro-tasks
├── interview_hard.py   # Advanced interview challenge (attempted)
├── inventory.py        # Inventory Management System
├── practice.py         # BankAccount rebuilt from blank slate
├── vault.py            # Secure Vault & Transaction System
└── README.md           # This file
```
