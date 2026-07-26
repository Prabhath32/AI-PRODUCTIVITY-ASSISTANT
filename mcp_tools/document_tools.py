import json


def search_documents():
    with open("data/documents.json", "r") as file:
        docs = json.load(file)

    return docs