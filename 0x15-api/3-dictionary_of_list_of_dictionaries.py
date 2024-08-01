#!/usr/bin/python3
"""Script uses a given REST API, to fetch data of all employees
    and exports data to JSON file
"""
import json
import requests
import sys


if __name__ == '__main__':
    api = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(f'{api}users').json()

    users_data = {}

    for user in users:
        todos = requests.get(
                                f'{api}todos',
                                params={'userId': user.get('id')}
                            ).json()
        users_data[user.get('id')] = [{
                                        "username": user.get('username'),
                                        "task": task.get('title'),
                                        "completed": task.get('completed')
                                      } for task in todos]

    with open('todo_all_employees.json', 'w', encoding='utf-8') as jsonf:
        json.dump(users_data, jsonf)
