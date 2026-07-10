"""
Weather briefing module.

Fetches a short summary of today's weather for Springfield, MO and returns a
single natural-language sentence for the daily briefing.

Uses only the standard library (urllib) and a free, key-less API:
    - Weather: https://api.open-meteo.com/v1/forecast
"""

import json
import urllib.request

_TIMEOUT_SECONDS = 5

# Springfield, MO
_LATITUDE = 37.2153
_LONGITUDE = -93.2982
_CITY = "Springfield"

_FALLBACK = "Could not get your local weather."

# Open-Meteo WMO weather codes mapped to spoken, day-summary descriptions.
_WEATHER_CODES = {
    0: "clear",
    1: "mostly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "foggy",
    48: "foggy",
    51: "drizzly",
    53: "drizzly",
    55: "drizzly",
    61: "rainy",
    63: "rainy",
    65: "very rainy",
    66: "icy",
    67: "icy",
    71: "snowy",
    73: "snowy",
    75: "heavy snow",
    77: "snowy",
    80: "rainy",
    81: "rainy",
    82: "stormy",
    85: "snowy",
    86: "snowy",
    95: "stormy",
    96: "stormy with hail",
    99: "stormy with hail",
}


def _get_json(url: str) -> dict:
    """Fetch and parse a JSON document."""
    request = urllib.request.Request(url, headers={"User-Agent": "life-manager"})
    with urllib.request.urlopen(request, timeout=_TIMEOUT_SECONDS) as response:
        return json.loads(response.read().decode("utf-8"))


def get_weather_summary() -> str:
    """
    Build a one- or two-sentence summary of today's weather for Springfield, MO.

    Returns "Could not get your local weather." if the forecast can't be
    retrieved so the briefing always says something about the weather.
    """
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={_LATITUDE}&longitude={_LONGITUDE}"
            "&daily=weathercode,temperature_2m_max,temperature_2m_min,"
            "precipitation_probability_max"
            "&temperature_unit=fahrenheit&forecast_days=1&timezone=auto"
        )
        daily = _get_json(url).get("daily", {})

        high = round(daily["temperature_2m_max"][0])
        low = round(daily["temperature_2m_min"][0])
        conditions = _WEATHER_CODES.get(daily["weathercode"][0], "mixed")
        precipitation = daily.get("precipitation_probability_max", [None])[0]

        summary = (
            f"Today in {_CITY} it'll be {conditions}, "
            f"with a high of {high} and a low of {low}."
        )
        if precipitation:
            summary += f" There's a {precipitation} percent chance of precipitation."
        return summary
    except Exception:
        # Network/API errors should still tell the user something.
        return _FALLBACK
