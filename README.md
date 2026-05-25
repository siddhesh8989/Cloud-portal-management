# Self-Service Cloud Resource Provisioning Portal

## Overview

This is a **Python Flask** academic project (SEAI). The main application lives entirely in `artifacts/cloud-portal/`.

**No database is used.** All data is stored in Python in-memory lists (resets on restart).

---

## Cloud Portal — Flask App (your project)

| File | Purpose |
|------|---------|
| `artifacts/cloud-portal/app.py` | Main Flask app, all routes |
| `artifacts/cloud-portal/policy_engine.py` | Policy validation (CPU/RAM/Storage/Region) |
| `artifacts/cloud-portal/data_storage.py` | In-memory storage using Python lists |
| `artifacts/cloud-portal/ml_model.py` | scikit-learn demand prediction |
| `artifacts/cloud-portal/requirements.txt` | Python dependencies |
| `artifacts/cloud-portal/README.md` | **Project README — start here** |
| `artifacts/cloud-portal/templates/` | HTML templates (Jinja2 + Tailwind CSS) |

### Run locally

```bash
pip install flask bcrypt scikit-learn numpy
python artifacts/cloud-portal/app.py
```

### Storage (in-memory, no database)

```python
# data_storage.py
users = []       # registered users
resources = []   # provisioned resources
violations = []  # policy violations
```

Data resets when the server restarts — perfect for demos.

---

## Node.js Monorepo (background infrastructure — ignore for your project)

The `lib/`, `artifacts/api-server/`, and `artifacts/mockup-sandbox/` folders are pre-existing Node.js scaffolding used by Replit's preview system. They are **not part of your Flask project** and do not use any database.

- `lib/db/` — disabled stub, not connected to anything
- `artifacts/api-server/` — lightweight proxy that forwards requests to Flask
- `artifacts/mockup-sandbox/` — Replit design tooling, unrelated to your project

---

## Active Workflow

- **Start application** → runs `python artifacts/cloud-portal/app.py` on port 5000
