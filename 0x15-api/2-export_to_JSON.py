#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(URL + "users/{}".format(user_id)).json()
    emp_name = user_info.get("username")
    todos = requests.get(URL + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todo]}, jsonfile)
