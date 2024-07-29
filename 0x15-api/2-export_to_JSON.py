#!/usr/bin/python3
"""Returns information about an employees TODO list
when given an employee ID"""

import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


def export_to_json(employee_id):
    """Fetches the employees todo list after giving a number request"""
    url_user = f"{url}/users/{employee_id}"
    url_todos = f"{url}/users/{employee_id}/todos"

    response_user = requests.get(url_user)
    if response_user.status_code != 200:
        print("Failed to fetch data for employee ID {}".format(employee_id))
        return

    EMPLOYEE_NAME = response_user.json().get("username")
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    response_todos = requests.get(url_todos)

    if response_todos.status_code != 200:
        print("Failed to fetch data for employee ID {}".format(employee_id))
        return

    for todo in response_todos.json():
        task_data = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": EMPLOYEE_NAME,
        }
        TASK_TITLE.append(task_data)

    json_data = {str(employee_id): TASK_TITLE}

    file_name = f"{employee_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    """Ensures the script acceps int as a parameter, the employee ID"""
    if len(sys.argv) != 2:
        print("Usage: python  script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    export_to_json(employee_id)
