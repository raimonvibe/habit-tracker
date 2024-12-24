import requests
import json
from datetime import datetime, timedelta
import os

# URL for the Pixela API
base_url = "https://pixe.la/v1/users"

def create_user(token, username):
    """Create a new user."""
    url = f"{base_url}"
    data = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        "thanksCode": "Thank you for the great API!"
    }
    response = requests.post(url, data=json.dumps(data))
    return response.json()

def create_graph(token, username, graph_id):
    """Create a new graph."""
    url = f"{base_url}/{username}/graphs"
    headers = {
        'Content-Type': 'application/json',
        "X-USER-TOKEN": token,
    }
    payload = {
        'id': graph_id,
        'name': "Coding-Hours",
        'unit': "hours",
        'type': "int",
        'color': "sora",
        'timezone': "Europe/Amsterdam",
        'isSecret': False
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def create_pixel(token, username, graph_id, date, quantity, optional_data=None):
    """Post a pixel to a graph."""
    url = f"{base_url}/{username}/graphs/{graph_id}"
    headers = {
        'Content-Type': 'application/json',
        "X-USER-TOKEN": token,
    }
    payload = {
        'date': date,
        'quantity': quantity
    }
    if optional_data:
        payload['optionalData'] = optional_data
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def main():
    # Configuration
    token = os.environ['SECRET_KEY']
    username = "raimonvibe"
    graph_id = "coding-hours"
    
    # Create user (this may fail if user already exists, which is fine)
    print("Creating user...")
    user_result = create_user(token, username)
    print(f"User creation result: {user_result}")
    
    # Create graph (this may fail if graph already exists, which is fine)
    print("\nCreating graph...")
    graph_result = create_graph(token, username, graph_id)
    print(f"Graph creation result: {graph_result}")
    
    print("\nCreating example data points...")
    # Example data points (hours of coding per day)
    data_points = [
        ("2024-01-21", "4"),  # Sunday
        ("2024-01-22", "6"),  # Monday
        ("2024-01-23", "5"),  # Tuesday
        ("2024-01-24", "7"),  # Wednesday
        ("2024-01-25", "4"),  # Thursday
        ("2024-01-26", "8"),  # Friday
        ("2024-01-27", "3"),  # Saturday
    ]
    
    # Create pixels for each data point
    for date, quantity in data_points:
        result = create_pixel(
            token=token,
            username=username,
            graph_id=graph_id,
            date=date.replace("-", ""),  # Format date as YYYYMMDD
            quantity=quantity
        )
        print(f"Created pixel for {date}: {result}")

if __name__ == "__main__":
    main()
