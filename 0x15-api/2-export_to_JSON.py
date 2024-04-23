#!/usr/bin/python3

import json
import requests
import sys

def get_employee_tasks(user_id):
    """
    Fetches tasks owned by a specific employee from the given user ID.
    
    Args:
        user_id (int): The ID of the user whose tasks are to be fetched.
        
    Returns:
        list: A list of dictionaries representing tasks owned by the employee.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': user_id}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch tasks for user {user_id}.")
        return []

    tasks = response.json()
    return tasks

def export_to_json(user_id, tasks):
    """
    Exports tasks owned by the employee to a JSON file.
    
    Args:
        user_id (int): The ID of the user.
        tasks (list): A list of dictionaries representing tasks owned by the employee.
    """
    filename = f"{user_id}.json"
    with open(filename, 'w') as file:
        json.dump({str(user_id): tasks}, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    tasks = get_employee_tasks(user_id)
    export_to_json(user_id, tasks)
