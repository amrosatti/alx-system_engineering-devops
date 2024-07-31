#!/usr/bin/python3
"""Script uses a given REST API, to fetch data

Args:
    sys.argv[1]: Employee ID

Returns:
    (str): Information about the employee's TODO list progress
"""
import csv
import requests
import sys


def main():
    """Driver function so the module won't run when imported
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(f'usage: {sys.argv[0]} <employee_id>')
        sys.exit(1)

    usr_id = int(sys.argv[1])
    api = 'https://jsonplaceholder.typicode.com/'
    usr = requests.get(f'{api}users/{usr_id}').json()
    usrname = usr.get('username')
    todos = requests.get(f'{api}todos', params={'userId': usr_id}).json()

    with open('{}.csv'.format(usr.get('id')), 'w', encoding='utf-8') as csvf:
        writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        [writer.writerow(
                    [usr_id, usrname, tsk.get('completed'), tsk.get('title')]
                ) for tsk in todos]


if __name__ == '__main__':
    main()
