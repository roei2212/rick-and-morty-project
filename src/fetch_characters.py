import requests
import csv

API_URL = "https://rickandmortyapi.com/api/character"

def fetch_characters():
    characters = []
    url = API_URL

    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for char in data["results"]:
            if (
                char["species"] == "Human"
                and char["status"] == "Alive"
                and char["origin"]["name"] == "Earth"
            ):
                characters.append({
                    "name": char["name"],
                    "location": char["location"]["name"],
                    "image": char["image"]
                })

        url = data["info"]["next"]

    return characters


def write_to_csv(characters, filename="results.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Location", "Image"])
        for char in characters:
            writer.writerow([char["name"], char["location"], char["image"]])


def main():
    print("Fetching characters from Rick and Morty API...")
    characters = fetch_characters()
    write_to_csv(characters)
    print("CSV created successfully!")


if __name__ == "__main__":
    main()