#!/usr/bin/python3
"""Script uses a given REST API, to fetch data

Args:
    sys.argv[1]: Employee ID

Returns:
    (str): Information about the employee's TODO list progress
"""

import sys
import requests


def main():
    """Driver function so the module won't run when imported
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print('usage: {} <employee_id>'.format(sys.argv[0]))
        return

    emp_id = int(sys.argv[1]) - 1
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    if users.status_code != 200:
        return

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    if todos.status_code != 200:
        return

    employees = users.json()
    if emp_id >= len(employees):
        return

    emp = employees[emp_id]
    todos = todos.json()

    emp_tasks = [tsk for tsk in todos if tsk.get('userId') == emp.get('id')]

    with open('{}.csv'.format(emp.get('id')), 'w', encoding='utf-8') as csvf:
        for task in emp_tasks:
            csvf.write(
                        '"{}","{}","{}","{}"\n'.format(
                                                        emp.get('id'),
                                                        emp.get('name'),
                                                        task.get('completed'),
                                                        task.get('title')
                                                    )
                        )


if __name__ == '__main__':
    main()
