# Stage 2 — Type Hints, File I/O, SQL & FastAPI Foundations

> **Status:** 🔄 IN PROGRESS
> **Duration:** Week 2–3 (Aug 5–15, 2026)
> **Goal:** Bridge Python Core to production FastAPI development

---

## What Will Be Learned

| Day | Topic | Deliverable | Why It Matters |
|:---|:---|:---|:---|
| 1 | Type hints (`Optional`, `Union`, `Callable`) | `type_hints.py` | FastAPI + Pydantic require these |
| 2–3 | File I/O + `pathlib` + context managers | `file_io.py` | Reading uploaded resumes in AI project |
| 4–5 | SQL (JOINs, GROUP BY, Window Functions) | `sql/` folder | Every backend interview has SQL round |
| 6–10 | FastAPI basics (routes, Pydantic, CRUD) | `fastapi_intro/` | The core of the career stack |

---

## File Structure

```
Stage-2/
├── README.md               # This file
├── type_hints.py            # Optional, Union, Callable, generics
├── file_io.py               # pathlib, context managers, CSV/JSON
│
├── sql/                     # SQL practice problems
│   ├── day_01_joins.sql
│   ├── day_02_groupby.sql
│   └── day_03_window.sql
│
├── fastapi_intro/           # First FastAPI application
│   ├── main.py              # Routes, request/response
│   ├── models.py            # Pydantic schemas
│   └── requirements.txt
│
└── DSA/                     # Daily DSA (continues from Stage-1)
    └── (1 problem per day)
```

---

## Connection to AI Resume Analyzer

| Stage 2 Skill | Production Use Case |
|:---|:---|
| `Optional[str]` | `class ResumeRequest(BaseModel): skills: Optional[list[str]]` |
| `pathlib.Path` | Reading uploaded PDF/DOCX resume files |
| `with open()` | Context managers for file upload handling |
| SQL JOINs | Querying analysis results across users + resumes tables |
| Window Functions | Ranking candidates by skill match score |
| FastAPI routes | `@app.post("/analyze")` endpoint |
| Pydantic models | Input validation before hitting Gemini API |
