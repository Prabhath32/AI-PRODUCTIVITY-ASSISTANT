import json


def search_emails():
    with open("data/emails.json", "r") as file:
        emails = json.load(file)

    return emails