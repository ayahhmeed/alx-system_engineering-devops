#!/usr/bin/python3

import csv
import requests
import sys


def get_tasks_by_user(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}/tasks".format(user_id)
    response = requests.get(url)
    tasks = response.json()
    return tasks


def get_user_info(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    return user


def export_to_csv(user_id, tasks, user):
    filename = "{}.csv".format(user_id)
    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for task in tasks:
            task_status = "True" if task["completed"] else "False"
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user["username"],
                "TASK_COMPLETED_STATUS": task_status,
                "TASK_TITLE": task["title"]
            })


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    tasks = get_tasks_by_user(user_id)
    user = get_user_info(user_id)

    if not tasks:
        print("No tasks found for user with id: {}".format(user_id))
        sys.exit(1)

    export_to_csv(user_id, tasks, user)
    print("Tasks exported to {}".format(user_id))


if __name__ == "__main__":
    main()
