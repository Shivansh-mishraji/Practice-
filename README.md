# Python Learning Journey 🚀

Welcome to my Python learning journey repository! This codebase tracks my progress as I build production-quality Python backend systems from scratch without copy-pasting or vibe-coding.

---

## 🎯 Active Sprint: Stage 1 — Python Core

Located in [`Stage-1/`](file:///c:/Users/91727/Desktop/Library-Practice/Stage-1):

- **`catalog.py`**: Smart Product Catalog system implementing private state (`_price`, `_discount`), `@property` getters, setters with `ValueError` validation, and read-only computed properties (`final_price`).
- **`vault.py`**: Secure Vault & Transaction system integrating OOP, private fields, custom decorators, and exception handling.
- **`decorators.py`**: Custom execution timer (`@timer`) and argument validator (`@validate_positive`) using `functools.wraps` and `*args/**kwargs`.
- **`bank.py`**: `BankAccount` class demonstrating `@property` validation, private state protection, and overdraft safety checks.
- **`inventory.py`**: CLI-based Inventory Management System with `@dataclass`, magic methods (`__repr__`, `__len__`), category filtering, and restocking alerts.

---

## 📁 Repository Structure

```
Python-Learning-Journey/
├── .agents/                    # Workspace mentor rules & progress tracking
├── Stage-1/                    # Active Sprint: Python Core modules
│   ├── catalog.py              # Product Catalog (@property getter/setter/read-only)
│   ├── vault.py                # Secure Vault Capstone
│   ├── decorators.py           # Custom timing & validation decorators
│   ├── bank.py                 # Bank Account property validation
│   ├── inventory.py            # Inventory System (@dataclass, CLI)
│   └── Topics.md               # Stage 1 Syllabus
└── archive/                    # Archived legacy practice scripts & notebooks
    ├── legacy_scripts/
    └── legacy_notebooks/
```

---

## 🚀 How to Run

Run any module directly from the repository root:

```bash
python Stage-1/catalog.py
python Stage-1/vault.py
python Stage-1/inventory.py
```
