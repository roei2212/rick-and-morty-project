import csv
import os

def write_to_csv(data, output_path="results.csv"):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Location", "Image"])

        for item in data:
            writer.writerow([item["name"], item["location"], item["image"]])