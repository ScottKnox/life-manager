# Feature: Weather Summary

## Goal

Add a short spoken summary of **today's** weather to the daily briefing, placed
right after the "Hello Scott." greeting.

## Scope

- Included: fetch today's forecast for a fixed location and produce a one- or
  two-sentence summary of what the full day will be like.
- Location is currently **hardcoded to Springfield, MO**.
- Out of scope: multi-day forecasts, severe-weather alerts, current-location
  detection, and per-user saved locations.

## Data

- **Weather:** Open-Meteo `https://api.open-meteo.com/v1/forecast` (free, no API
  key) using `daily` fields: `weathercode`, `temperature_2m_max`,
  `temperature_2m_min`, `precipitation_probability_max` with `forecast_days=1`.
- No MongoDB collections are used.
- Implemented with the standard library (`urllib`) — no new dependencies.

## Briefing Output

One or two sentences describing the day's conditions, high/low, and chance of
precipitation.

> Example: "Today in Springfield it'll be partly cloudy, with a high of 88 and a
> low of 65. There's a 40 percent chance of precipitation."

If the forecast can't be retrieved, the briefing says:

> "Could not get your local weather."

## Acceptance Criteria

- [ ] `/briefing` returns the greeting followed by a full-day weather summary.
- [ ] The summary covers the whole current day (high, low, conditions).
- [ ] A network/API failure yields "Could not get your local weather."
- [ ] No new third-party packages are added.

## Open Questions

- Location is hardcoded; a later iteration should use the caller's real location.
- Units: currently Fahrenheit; make configurable later if needed.
