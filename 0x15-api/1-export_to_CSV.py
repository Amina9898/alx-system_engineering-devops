#!/usr/bin/python3
"""
This is a script that fetches employeie TODO list
informaation from an API
"""


import csv
import requests
import sys


def export_to_csv(user_id):
    """ function that fetches the required todo info """

    URL = "https://jsonplaceholder.typicode.com"

    user_info = requests.get(f"{URL}/users/{user_id}")
    user_info = user_info.json()
    username = user_info.get('username')

    todo = requests.get(f"{URL}/todos?userId={user_id}")
    todo = todo.json()

    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todo:
            if task['completed']:
                status = True
            else:
                status = False
            writer.writerow([user_id, username, status, task['title']])


if __name__ == "__main__":

    user_id = int(sys.argv[1])
    export_to_csv(user_id)
