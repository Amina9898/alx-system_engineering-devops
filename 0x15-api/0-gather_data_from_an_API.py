#!/usr/bin/python3
"""
This is a script that fetches employeie TODO list
informaation from an API
"""


import requests
import sys


def fetch_employee_todo(employee_id):
    """ function that fetches the required todo info """
    URL = "https://jsonplaceholder.typicode.com"

    user_info = requests.get(f"{URL}/users/{employee_id}")
    user_info = user_info.json()
    emp_name = user_info.get('name')

    todo = requests.get(f"{URL}/todos?userId={employee_id}")
    todo = todo.json()

    total = len(todo)
    completed = sum(1 for task in todo if task['completed'])

    print(f"Employee {emp_name} is done with tasks({completed}/{total}):")

    for task in todo:
        if task['completed']:
            print("\t {}".format(task['title']))


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    fetch_employee_todo(employee_id)
