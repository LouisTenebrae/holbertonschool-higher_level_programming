#!/usr/bin/python3
"""CSV"""
import csv
import json

def convert_csv_to_json(csvfile):
    """Convert CSV to JSON"""
    try:
        with open(csvfile, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        with open("data.json", "w") as file:
            json.dump(data, file)

        return True
    
    except Exception:
        return False
