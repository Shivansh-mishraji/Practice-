# AI-Powered Resume & Job Description Analyzer
## Minor Project — V1 Project Specification & Roadmap

**Project Type:** Minor Project
**Target Completion:** 1st Week of September 2026
**Team Size:** 4 Members
**Development Approach:** Agile / Scrum-inspired
**Primary Goal:** Build a working, cloud-deployed AI-powered web application that analyzes a resume against a specific Job Description (JD) and provides explainable, personalized improvement suggestions.

---

## 1. Project Vision

An AI-Powered Resume & Job Description Analyzer that helps students and job seekers understand how well their resume matches a particular job opportunity.

The user provides:
1. **Resume** — PDF/DOCX
2. **Target Job Description** — pasted by the user

The system determines:
- How closely the resume matches the job
- Which required skills are present/missing
- Whether projects and experience are relevant
- Important keywords from the JD
- Weak areas of the resume
- Personalized suggestions for improvement

**Core workflow:**
```
Resume + Job Description → Resume Parsing → JD Analysis → Matching → Scoring → AI Recommendations → Final Report
```

---

## 2. Problem Statement

Students submit the same resume to multiple jobs, but different jobs have different technical requirements, skills, responsibilities, and keywords. The system solves this by comparing the resume against a specific JD and providing actionable feedback.

---

## 3. Main Objective

> Upload resume, paste JD, receive structured analysis showing resume-job match, strengths, missing requirements, weaknesses, and AI-generated improvement suggestions.

---

## 4. V1 Scope — MUST HAVE

### Resume
- PDF upload, DOCX upload, file validation, text extraction, basic info extraction

### Job Description
- Text input/paste, JD cleaning, requirement extraction, skill/keyword identification

### Analysis
- Resume ↔ JD comparison, skill matching, keyword matching, missing skills identification
- Basic experience/project relevance analysis
- Overall match score, category-wise scores, AI-generated suggestions

### Frontend
- Home page, resume upload, JD input, Analyze button, loading state, results dashboard, error messages

### Backend
- FastAPI, REST API, Pydantic validation, resume processing, analysis service, AI integration
- Error handling, logging, API documentation

### Deployment
- Frontend deployed, backend deployed, working public URL, env vars configured

### Project Engineering
- Git/GitHub, README, basic testing, project report, architecture diagram, flowchart, use case diagram, PPT, demo

---

## 5. Explicitly OUT OF SCOPE for V1

Payment gateway, subscription, complex auth, advanced user profiles, Redis, Celery, microservices, Kubernetes, complex RAG, job scraping, LinkedIn integration, automatic applications, interview simulator, cover-letter generator, career chatbot, advanced ML training, complex recommendation engine.

*These are V2 / Major Project features.*

---

## 6. User Flow

```
Step 1: Open Website
Step 2: Upload Resume (PDF/DOCX)
Step 3: Paste Job Description
Step 4: Click "Analyze My Resume"
Step 5: Backend Processing (validate → extract → clean → match → score → AI → recommend)
Step 6: View Results (score, skill match, keyword match, strengths, missing skills, recommendations)
```

---

## 7. Example Output

**Resume–Job Match: 78/100**

| Category | Score |
|:---|:---|
| Technical Skills | 85% |
| Job Keywords | 75% |
| Projects | 80% |
| Experience Relevance | 70% |
| Education | 90% |

**Strong Matches:** Python, FastAPI, REST APIs, SQL, Git

**Missing / Weak Requirements:** Docker, PostgreSQL, Automated Testing, Cloud deployment

**AI Recommendations:**
1. Add relevant Docker experience if you have actually used Docker.
2. Mention PostgreSQL explicitly if your projects use it.
3. Add measurable outcomes to project descriptions.
4. Highlight backend API development more clearly.
5. Add testing experience where applicable.

---

## 8. Design Principle — Explainable Analysis

The system must explain **why** a score is given, not just show a number.

| Job Requirement | Resume Evidence | Result |
|:---|:---|:---|
| Experience with FastAPI and REST APIs | "Developed REST APIs using FastAPI for a resume analysis application." | ✅ Strong Match |
| Experience with Docker | No relevant evidence found. | ❌ Missing Requirement |

---

## 9. Technology Stack

| Layer | Technology |
|:---|:---|
| Frontend | React.js |
| Backend | Python + FastAPI |
| Resume Parsing | PyMuPDF (PDF), python-docx (DOCX) |
| Database | SQLite (V1), PostgreSQL (V2) |
| AI | Suitable AI API with free tier (modular — swappable) |
| Version Control | Git + GitHub |
| API Testing | FastAPI Swagger / Postman |
| Deployment | Cloud (HTTPS, env vars, no hardcoded secrets) |

---

## 10. High-Level Architecture

```
                    USER
                      │
                      ▼
              ┌───────────────┐
              │ React Frontend│
              └───────┬───────┘
                      │ HTTP/HTTPS
                      ▼
              ┌───────────────┐
              │ FastAPI Backend│
              └───────┬───────┘
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
   Resume Parser   JD Parser   Database
          │           │
          └─────┬─────┘
                ▼
       ┌──────────────────┐
       │  Matching Engine  │
       │  Skills/Keywords  │
       │  Requirements     │
       └────────┬─────────┘
                ▼
       ┌──────────────────┐
       │  Scoring Engine   │
       └────────┬─────────┘
                ▼
       ┌──────────────────┐
       │  AI Analysis &    │
       │  Recommendations  │
       └────────┬─────────┘
                ▼
       ┌──────────────────┐
       │ Results Dashboard │
       └──────────────────┘
```

---

## 11. Backend Folder Structure

```
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── resume.py
│   │   ├── analysis.py
│   │   └── health.py
│   │
│   ├── services/
│   │   ├── resume_parser.py
│   │   ├── jd_parser.py
│   │   ├── matcher.py
│   │   ├── scorer.py
│   │   └── ai_analyzer.py
│   │
│   ├── schemas/
│   │   ├── resume.py
│   │   └── analysis.py
│   │
│   ├── models/
│   │   └── database_models.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   └── database/
│       └── database.py
│
├── tests/
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md
```

**Principle:** `API layer ≠ business logic ≠ AI logic ≠ database logic`

---

## 12. API Design (V1)

### Health Check
```
GET /health
```
Returns backend status.

### Resume Analysis
```
POST /api/v1/analyze
Input: Resume file + Job Description text
```
```json
{
  "overall_score": 78,
  "skill_match": 85,
  "keyword_match": 75,
  "project_relevance": 80,
  "strengths": [],
  "missing_skills": [],
  "recommendations": []
}
```

---

## 13. Scoring System

| Category | Weight |
|:---|:---|
| Technical Skills | 30% |
| Job Keywords | 20% |
| Projects | 20% |
| Experience/Relevance | 20% |
| Education | 10% |

**Principle:** Deterministic logic calculates the score. AI explains it.

---

## 14. Hybrid AI Architecture

| Layer | Responsibility |
|:---|:---|
| **Deterministic System** | File validation, text extraction, keyword detection, skill matching, score calculation, missing requirements |
| **AI Layer** | Context understanding, explaining weaknesses, personalized suggestions, natural-language recommendations |

---

## 15. AI Prompt Design Principle

AI receives **structured information**, not raw documents:

```
TARGET JOB: Backend Developer

JOB REQUIREMENTS: Python, FastAPI, REST APIs, PostgreSQL, Docker, Testing

RESUME SKILLS: Python, FastAPI, SQL, Git

MATCH RESULTS:
Python: MATCH
FastAPI: MATCH
REST APIs: MATCH
PostgreSQL: MISSING
Docker: MISSING
Testing: MISSING
```
→ Generate structured recommendations from this.

---

## 16. Database Schema (V1 — SQLite)

**Table: `analyses`**

| Column | Type |
|:---|:---|
| id | INTEGER PRIMARY KEY |
| resume_filename | TEXT |
| job_title | TEXT |
| job_description | TEXT |
| overall_score | INTEGER |
| skill_score | INTEGER |
| keyword_score | INTEGER |
| project_score | INTEGER |
| experience_score | INTEGER |
| education_score | INTEGER |
| result_json | TEXT |
| created_at | DATETIME |

*Designed so `user_id` can be added in V2 without restructuring.*

---

## 17. Security Requirements (V1)

- File type validation (PDF/DOCX only)
- File size limit
- Input validation via Pydantic
- API error handling
- API key protection via `.env`
- `.gitignore` for secrets
- Do NOT expose API keys to frontend
- Do NOT store resumes permanently (process and discard)
- Basic rate limiting if practical

---

## 18. Team Structure

| Role | Member |
|:---|:---|
| Product Owner | Mentor / Guide |
| Scrum Master + Technical Lead | **Shivansh** |
| Backend & AI Developer | **Shivansh** |
| Frontend Developer | Member 2 |
| Documentation & Research Lead | Member 3 |
| Testing & Presentation Lead | Member 4 |

---

## 19. Sprint Timeline

### Sprint 0 — Project Setup (Aug 8–9)
**Goal:** Freeze requirements, setup development environment
- Finalize architecture + FastAPI project structure
- Create GitHub repository
- All members understand scope and responsibilities

### Sprint 1 — Resume + JD Processing (Aug 10–16)
**Goal:** Input-processing pipeline
- Resume upload API (PDF + DOCX parsing, file validation)
- JD input API (text cleaning, requirement extraction)
- Frontend: upload UI + submit button
- Tests: valid PDF, valid DOCX, invalid file, empty JD, large file

**Deliverable:** Backend can successfully extract/process both resume and JD.

### Sprint 2 — Matching + Scoring (Aug 17–23)
**Goal:** Core analysis engine
- Skill extraction, keyword extraction, requirement matching
- Missing skills identification, scoring system
- Frontend: results page with scores + strengths + missing skills

**Deliverable:** Working Resume ↔ JD matching WITHOUT depending on AI.

### Sprint 3 — AI Integration (Aug 24–30)
**Goal:** AI-generated personalized recommendations
- AI API integration, prompt design, structured AI output
- AI error handling, response validation
- Frontend: AI suggestions section, UI polishing

**Deliverable:** Complete working AI-powered analyzer.

### Sprint 4 — Deployment + Finalization (Aug 31 – Sep 6)
**Goal:** Demonstration-ready product
- Production config, env vars, security review, logging
- Docker (if practical), cloud deployment
- End-to-end testing, final report, PPT, demo script

**Final Deliverable:** Publicly accessible, working, documented, demonstrated V1.

---

## 20. V1 Definition of Done

### Functionality
- [ ] Resume PDF upload works
- [ ] DOCX upload works
- [ ] Job Description input works
- [ ] Resume parsing works
- [ ] JD processing works
- [ ] Matching works
- [ ] Score is generated
- [ ] Missing skills identified
- [ ] AI recommendations work
- [ ] Results displayed clearly

### Engineering
- [ ] FastAPI backend works
- [ ] React frontend works
- [ ] Input validation exists
- [ ] Errors are handled
- [ ] Secrets are protected
- [ ] Basic tests exist
- [ ] GitHub repository is organized
- [ ] README is complete

### Deployment
- [ ] Frontend deployed
- [ ] Backend deployed
- [ ] API connected to frontend
- [ ] Public URL works

### Documentation
- [ ] Abstract, SRS, problem statement, objectives
- [ ] Architecture diagram, flowchart, use case diagram, database diagram
- [ ] Testing report, user manual, PPT

---

## 21. V1 → V2 → SaaS Roadmap

```
V1 (Minor Project)
Resume + JD → Analysis → Score + Suggestions
Stack: React + FastAPI + SQLite + AI API + Cloud

V2 (Major Project)
+ User Auth + Resume History + Multiple JD Templates
+ PostgreSQL + Redis + Celery + Advanced RAG
+ Cover Letter Generator + LinkedIn Integration

SaaS
+ Subscription + Billing + API Access
+ Enterprise Plans + Job Scraping + Interview Simulator
```

---

## 22. Demo Flow (Final Presentation ~10 mins)

1. Open deployed website
2. Upload prepared PDF resume
3. Paste realistic Backend Developer JD
4. Click Analyze → show loading state
5. Show results: overall score, category scores, strengths, missing skills, AI suggestions
6. Explain architecture: React → FastAPI → Parser → Matcher → Scorer → AI → Results
7. Explain engineering: GitHub, API design, testing, error handling, cloud deployment
