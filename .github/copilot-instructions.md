---
applyTo: "**"
---

# Life Manager — Copilot Instructions

## Product

Life Manager is a personal automation app that aggregates daily life details
(weather, calendar, bills, meds, birthdays, budget flags, etc.) into a single
spoken daily briefing. The target pipeline is **phone → cloud → voice**.

See [docs/product-goals.md](../docs/product-goals.md) for the overall vision and
[docs/features/](../docs/features/) for specifications of larger features.

## Tech Stack

- **Backend:** Python 3.9+, FastAPI, Uvicorn
- **Data:** MongoDB (data is reset manually when needed — no migrations required)

## Conventions

- Each briefing module plugs into `build_briefing()` in [app.py](../app.py) and
  appends one or two sentences to `parts`.
- Keep endpoints small; push aggregation logic into dedicated modules.
- Prefer standard library and existing dependencies before adding new packages.

## Working Agreements

- Prioritize low-risk, incremental changes first to avoid rework.
- No backward-compatibility work is required; Mongo data can be reset manually.
- When adding a larger feature, first add or update a spec in
  [docs/features/](../docs/features/), then implement against it.

## Run & Test

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

API available at `http://localhost:8000`.
