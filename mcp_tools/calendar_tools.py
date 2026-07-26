import json


def get_meetings():
    with open("data/meetings.json", "r") as file:
        meetings = json.load(file)

    return meetings