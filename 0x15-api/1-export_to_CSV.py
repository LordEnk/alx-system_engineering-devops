#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": u_id}).json()

    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for completed, title in done_tasks:
            completed_status = 'Yes' if completed else 'No'
            csv_writer.writerow([user_id, employee_name, completed_status, title])
