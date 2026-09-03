# Autonomous Multi-Agent Code Review & Security Auditor

A production-style autonomous system for reviewing GitHub Pull Requests using specialized AI agents, deterministic security & static analysis tools, risk-based confidence routing, and Human-in-the-Loop (HITL) approval.

---

## Architecture Overview

```text
Developer
   │
   │ git push
   ▼
GitHub Pull Request
   │
   │ Webhook
   ▼
FastAPI Backend
   │
   ▼
LangGraph Orchestrator
   │
   ├──────────────────────┐
   ▼                      ▼
Analyzer Agent       Security Agent
   │                      │
   └──────────┬───────────┘
              ▼
       Lead Reviewer Agent
              │
              ▼
       Confidence / Risk Router
          /             \
         /               \
        ▼                 ▼
   Auto Publish       Human Review
                         │
                    Approve/Edit/Reject
                         │
                         ▼
                    GitHub API
                         │
                         ▼
                  PR Review Comments
```

---

## Quick Start (Section 1)

### 1. Environment Setup
```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1    # On Windows PowerShell
# or
source .venv/bin/activate       # On Linux/macOS
```

### 2. Run Tests
```bash
pytest tests/unit/test_health.py -v
```

### 3. Run FastAPI Dev Server
```bash
uvicorn app.main:app --reload
```

Check health status:
```bash
curl http://localhost:8000/health
```
or open `http://localhost:8000/docs` in your browser.
