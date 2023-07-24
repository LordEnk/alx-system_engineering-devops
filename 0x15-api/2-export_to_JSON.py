#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
from urllib import request
import requests
import sys
if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url+"users/{}".format(u_id)).json()
    username = user.get("username")
    todos = requests.get(url+"todos", params={"userId": u_id}).json()

    tasks_data = [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todos_data]
    json_filename = f'{user_id}.json'
    with open(json_filename, 'w') as json_file:
        json.dump({str(user_id): tasks_data}, json_file, indent=4)
