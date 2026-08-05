# Stage 1 — Python Core Foundations

> **Status:** ✅ COMPLETED
> **Duration:** Week 1–2 (Aug 2–5, 2026)
> **Goal:** Master Python core patterns used in backend engineering

---

## What Was Learned

| Concept | File | Key Pattern |
|:---|:---|:---|
| OOP + `__repr__` + `__len__` | `projects/inventory.py`, `assessment/OOPs.py` | Class design, dunder methods |
| `@property` getter/setter | `projects/bank.py`, `projects/catalog.py` | Private state, validation |
| Exception handling | `projects/vault.py`, `assessment/Exceptions.py` | `raise ValueError`, custom exceptions |
| Decorators + closures | `practice/decorators.py`, `assessment/Decorators.py` | `@wraps`, `*args/**kwargs`, closures |
| Generators + `yield` | `projects/generator.py` | Lazy evaluation, generator chaining |
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
├── README.md               # This file
├── Topics.md               # Detailed topic notes
│
├── projects/               # Main project files (graded tasks)
│   ├── inventory.py        # Inventory Management System
│   ├── bank.py             # BankAccount with @property validation
│   ├── vault.py            # Secure Vault & Transaction System
│   ├── catalog.py          # Smart Product Catalog
│   └── generator.py        # Lazy Log Stream Pipeline (3 chained generators)
│
├── practice/               # Practice & skill-building
│   ├── decorators.py       # Custom timing and validation decorators
│   └── practice.py         # BankAccount rebuilt from blank slate
│
├── interview/              # Interview preparation
│   ├── interview_drills.py # Micro-tasks (RateLimiter, require_auth, APIResponse)
│   └── interview_hard.py   # Advanced challenge (attempted, reset to micro-tasks)
│
├── Assessment/             # Self-assessment with review comments
│   ├── OOPs.py             # OOP concepts assessment
│   ├── Properties.py       # @property + @dataclass assessment
│   ├── Exceptions.py       # Exception handling assessment
│   └── Decorators.py       # Decorators + closures assessment
│
└── DSA/                    # Daily DSA practice
    └── two-sum.py          # Day 1: Two Sum — HashMap O(n)
```
