#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    try:
        users_response = requests.get(f'{base_url}/users')
        users_data = users_response.json()

        all_tasks_data = {}
        for user_data in users_data:
            employee_id = user_data.get('id')
            employee_name = user_data.get('name', 'Unknown Employee')

            todos_response = requests.get(f'{base_url}/todos', params={"userId": employee_id})
            todos_data = todos_response.json()

            tasks_data = [{"username": employee_name, "task": task['title'], "completed": task['completed']} for task in todos_data]

            all_tasks_data[str(employee_id)] = tasks_data

        json_filename = 'todo_all_employees.json'
        with open(json_filename, 'w') as json_file:
            json.dump(all_tasks_data, json_file, indent=4)
    except requests.exceptions.RequestException as e:
