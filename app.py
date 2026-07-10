"""
Daily Briefing Backend — v1 (skeleton)

One endpoint that will eventually aggregate weather, calendar, bills,
meds, birthdays, etc. into a single spoken briefing. Right now it just
says hello, to prove the whole pipeline (phone -> cloud -> voice) works.

Local test:
    pip install -r requirements.txt
    uvicorn app:app --reload
    curl http://localhost:8000/briefing
"""

from fastapi import FastAPI

from weather import get_weather_summary

app = FastAPI()


@app.get("/briefing")
def get_briefing():
    text = build_briefing()
    return {"text": text}


def build_briefing() -> str:
    """
    This function is where every future module plugs in:
    weather, calendar, bills, meds, birthdays, budget flags, etc.
    Each module just appends a sentence or two to `parts`.
    """
    parts = []

    parts.append("Hello Scott.")

    parts.append(get_weather_summary())

    # --- future modules go here, e.g. ---
    # parts.append(get_calendar_summary())
    # parts.append(get_bills_due_summary())

    return " ".join(parts)
