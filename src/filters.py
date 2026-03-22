def filter_characters(characters):
    """Filter characters by:
    - Species = Human
    - Status = Alive
    - Origin = Earth
    """
    filtered = []

    for c in characters:
        if (
            c.get("species") == "Human"
            and c.get("status") == "Alive"
            and c.get("origin", {}).get("name", "").lower().startswith("earth")
        ):
            filtered.append({
                "name": c.get("name"),
                "location": c.get("location", {}).get("name"),
                "image": c.get("image")
            })

    return filtered