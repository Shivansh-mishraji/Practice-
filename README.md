<div align="center">

# Python Learning Journey
### GSAEB — Global Software & AI Engineering Blueprint
**Shivansh Mishra | BBD University | Target: Backend AI Engineering Internship**

</div>

---

## What This Repo Is

This is my **active training log** — not a portfolio, not a tutorial dump.

Every file here was:
1. Written from memory, without copy-pasting
2. Reviewed like a real code review (bugs listed by severity)
3. Fixed by understanding the bug, not just applying the fix
4. Committed with conventional commit messages

**Goal**: Land a Backend AI Engineering internship within 2–3 months by building production-quality skills through deliberate, hands-on practice.

---

## Progress Tracker

### Stage 1 — Python Core (Week 1–2)

| Concept | Status | File |
|:---|:---:|:---|
| OOP — Classes, `__init__`, `__repr__`, `__len__` | ✅ | `Stage-1/inventory.py` |
| `@dataclass` | ✅ | `Stage-1/inventory.py` |
| `@property` getter + setter + read-only | ✅ | `Stage-1/bank.py` |
| Private attributes (`_attr`) convention | ✅ | `Stage-1/bank.py` |
| Exception handling — `raise`, `try/except` | ✅ | `Stage-1/vault.py` |
| Decorators — `functools.wraps`, `*args/**kwargs` | ✅ | `Stage-1/decorators.py` |
| Decorator stacking | ✅ | `Stage-1/decorators.py` |
| Git — `add`, `commit`, `log`, `.gitignore` | ✅ | `.gitignore` |
| Conventional commit messages | ✅ | `git log --oneline` |
| Closures — LEGB, `nonlocal` | 🔄 Next | |
| Generators — `yield`, lazy evaluation | ⏳ | |
| Type hints — `Optional`, `Union`, `Callable` | ⏳ | |
| File handling — `pathlib`, JSON, CSV | ⏳ | |
| Logging — structured, handlers | ⏳ | |
| Modules and packages — `src/` layout | ⏳ | |

---

### Stage 2 — Backend Engineering (Week 3–6)

| Topic | Status |
|:---|:---:|
| Git advanced — branches, rebase | ⏳ |
| SQL intermediate — JOINs, window functions | ⏳ |
| FastAPI — routes, Pydantic, dependency injection | ⏳ |
| FastAPI — JWT auth, middleware, pagination | ⏳ |
| PostgreSQL + SQLAlchemy + Alembic | ⏳ |
| pytest + mocking | ⏳ |
| Docker + docker-compose | ⏳ |

---

### Stage 3 — AI Engineering (Week 7–8)

| Topic | Status |
|:---|:---:|
| Gemini API — generation, structured output, streaming | ⏳ |
| Embeddings — generate, cosine similarity | ⏳ |
| ChromaDB — store and query vectors | ⏳ |
| RAG pipeline — chunk → embed → retrieve → generate | ⏳ |
| Deploy on Render / Railway | ⏳ |
| GitHub Actions CI | ⏳ |

---

## Files Built

| File | Concepts Covered |
|:---|:---|
| `Stage-1/inventory.py` | OOP, `@dataclass`, `__repr__`, `__len__`, exception handling, CLI |
| `Stage-1/bank.py` | Standard class, `@property` getter/setter, private `_balance`, overdraft protection |
| `Stage-1/decorators.py` | Closures, `functools.wraps`, `*args/**kwargs`, decorator stacking |
| `Stage-1/vault.py` | Integration — OOP + decorators + exceptions + private state management |

---

## Commit Convention

```
feat:     new feature or file
fix:      bug fix
refactor: restructure, no behavior change
chore:    setup, config, tooling
docs:     documentation only
test:     test files only
```

---

## Roadmap

```
Week 1  [###################.]  95%  Python Core
Week 2  [...................]   0%  Professional Python
Week 3  [...................]   0%  Git + SQL + FastAPI entry
Week 4  [...................]   0%  FastAPI core
Week 5  [...................]   0%  PostgreSQL + SQLAlchemy
Week 6  [...................]   0%  pytest + Docker
Week 7  [...................]   0%  Gemini API + RAG
Week 8  [...................]   0%  Deploy + Apply
```

*Updated after every session. Full tracking in [`.agents/AGENTS.md`](.agents/AGENTS.md).*
