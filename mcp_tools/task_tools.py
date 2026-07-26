import json


def create_task(task):

    with open("data/tasks.json", "r") as file:
        tasks = json.load(file)

    tasks.append(task)

    with open("data/tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return "Task created successfully."
