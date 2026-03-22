import requests
from writer import write_to_csv

def main():
    print("Fetching characters from local API...")
    response = requests.get("http://localhost:8000/characters")
    response.raise_for_status()

    characters = response.json()
    write_to_csv(characters)

    print("CSV created successfully!")

if __name__ == "__main__":
    main()