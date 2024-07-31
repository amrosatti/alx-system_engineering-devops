#!/usr/bin/python3
"""Script uses a given REST API, to fetch data by emplyee
    and exports data to JSON file
"""
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(f'usage: {sys.argv[0]} <employee_id>')
        sys.exit(1)

    user_id = int(sys.argv[1])
    api = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f'{api}users/{user_id}').json()
    todos = requests.get(f'{api}todos', params={'userId': user_id}).json()

    user_data = {user.get('id'): list(
                                 [{
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": user.get('username')
                                  } for task in todos]
                                )}

    with open(f'{user.get("id")}.json', 'w', encoding='utf-8') as jsonf:
        json.dump(user_data, jsonf)
