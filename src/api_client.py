import requests
import time

BASE_URL = "https://rickandmortyapi.com/api/character"


def fetch_all_characters():
    """Fetch all characters from the API (handles pagination)."""
    results = []
    url = BASE_URL

    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        results.extend(data["results"])
        url = data["info"]["next"]  # next page

        # Prevent hitting rate limits
        time.sleep(0.25)

    return results