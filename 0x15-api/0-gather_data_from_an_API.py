#!/usr/bin/python3
"""Script uses a given REST API, to fetch data

Args:
    argv[1]: Employee ID

Returns:
    (str): Information about the employee's TODO list progress
"""

from sys import argv
import requests


def main():
    """Driver function so the module won't run when imported
    """
    if len(argv) != 2 or not argv[1].isdigit():
        print('usage: {} <employee_id>'.format(argv[0]))
        return

    emp_id = int(argv[1]) - 1
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    if users.status_code != 200:
        return

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    if todos.status_code != 200:
        return

    employees = users.json()
    if emp_id >= len(employees):
        return

    employee = employees[emp_id]
    todos = todos.json()

    n_done, n_total = 0, 0
    done_titles = []

    for task in todos:
        if task.get('userId') == employee.get('id'):
            n_total += 1
            if task.get('completed'):
                n_done += 1
                done_titles.append(task.get('title'))

    print(f"Employee {employee.get('name')} is done with",
          f"tasks({n_done}/{n_total}):")

    [print('\t {}'.format(title)) for title in done_titles]


if __name__ == '__main__':
    main()
