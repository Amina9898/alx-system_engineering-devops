#!/usr/bin/python3
"""
This is a script that fetches employeie TODO list
informaation from an API
"""


import csv
import requests
import sys


def export_to_csv(employee_id):
    """ function that fetches the required todo info """

    URL = "https://jsonplaceholder.typicode.com"

    user_info = requests.get(f"{URL}/users/{employee_id}")
    user_info = user_info.json()
    emp_name = user_info.get('name')

    todo = requests.get(f"{URL}/todos?userId={employee_id}")
    todo = todo.json()

    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todo:
            if task['completed']:
                status = "True"
            else:
                status = "False"
            writer.writerow([employee_id, emp_name, status, task['title']])


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
