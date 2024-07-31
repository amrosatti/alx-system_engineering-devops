#!/usr/bin/python3
"""Script uses a given REST API, to fetch ToDo list info for a given id
"""
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

    completed_titles = [task.get('title') for task in todos
                        if task.get('completed')]

    print(f'Employee {user.get("name")} is done with',
          f'tasks({len(completed_titles)}/{len(todos)}):')

    [print(f'\t {title}') for title in completed_titles]
