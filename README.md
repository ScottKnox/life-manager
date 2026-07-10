# Life Manager

A personal automation app that aggregates the details of daily life — weather, calendar, bills, meds, birthdays, budget flags, and more — into a single spoken daily briefing.

The long-term goal is a simple pipeline: **phone → cloud → voice**, delivering one concise summary of everything you need to know for the day.

## Status

Early skeleton. The backend currently exposes a single `/briefing` endpoint that returns a placeholder greeting, proving the end-to-end pipeline works. Individual modules (weather, calendar, bills, etc.) plug into `build_briefing()` as they are built.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
pip install -r requirements.txt
```

### Run

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`.

## Usage

Fetch the current briefing:

```bash
curl http://localhost:8000/briefing
```

Response:

```json
{ "text": "Hello Scott." }
```

## Roadmap

- [ ] Weather summary
- [ ] Calendar summary
- [ ] Bills due summary
- [ ] Medication reminders
- [ ] Birthday reminders
- [ ] Budget flags
- [ ] Voice delivery (phone → cloud → voice)
