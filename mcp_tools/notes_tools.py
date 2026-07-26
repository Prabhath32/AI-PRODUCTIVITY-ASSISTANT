import json


def search_notes():
    with open("data/notes.json", "r") as file:
        notes = json.load(file)

    return notes