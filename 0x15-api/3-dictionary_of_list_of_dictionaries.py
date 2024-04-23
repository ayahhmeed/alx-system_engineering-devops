import json
import requests

def get_user_tasks(user_id):
    """tasks for a specific user"""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch tasks for user {user_id}")
        return []

def main():
    # List of user IDs
    user_ids = range(1, 11)

    # Dictionary to store tasks
    all_tasks = {}

    # Fetch tasks for each user and store them in the dictionary
    for user_id in user_ids:
        tasks = get_user_tasks(user_id)
        all_tasks[str(user_id)] = tasks

    # Write the dictionary to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

if __name__ == "__main__":
    main()

