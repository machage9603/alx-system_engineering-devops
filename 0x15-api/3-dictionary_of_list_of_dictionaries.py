#!/usr/bin/python3
"""Returns information about an employees TODO list
when given an employee ID"""

import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    """Fetches the employees todo list after giving a number request"""
    url_user = f"{url}/users"
    url_todos = f"{url}/todos"

    response_user = requests.get(url_user).json()
    response_todos = requests.get(url_todos).json()

    todos_dict = {}

    for user in response_user:
        user_id = str(user.get('id'))
        username = user.get('username')
        todos_dict[user_id] = []

        for todo in response_todos:
            if str(todo.get('userId')) == user_id:
                todo_data = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                todos_dict[user_id].append(todo_data)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todos_dict, json_file)
