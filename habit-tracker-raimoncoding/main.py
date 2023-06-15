import requests
import json
from datetime import datetime


# URL for the Pixela API.
base_url = "https://pixe.la/v1/users"

# Get the current date in the format yyyyMMdd
current_date = datetime.now().strftime('%Y%m%d')

# Creating a user.
def create_user(token, username, agree_terms_of_service, not_minor, thanks_code):
    """Create a new user.

    Args:
    token (str): A token string used to authenticate as a user to be created.
    username (str): User name for this service.
    agree_terms_of_service (str): Specify yes or no whether you agree to the terms of service.
    not_minor (str): Specify yes or no as to whether you are not a minor or if you are a minor and you have the parental consent of using this service.
    thanks_code (str): Set thanks-code.

    Returns:
    dict: API response.
    """
    url = f"{base_url}"

    data = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agree_terms_of_service,
        "notMinor": not_minor,
        "thanksCode": thanks_code
    }

    response = requests.post(url, data=json.dumps(data))

    return response.json()




# Creating a graph.
def create_graph(token, username, graph_id, graph_name, unit, type, color, timezone, is_secret):
    """Create a new graph.

    Args:
    token (str): A token string used to authenticate as a user.
    username (str): User name for this service.
    graph_id (str): ID for identifying the pixelation graph.
    name (str): Name of the pixelation graph.
    unit (str): Unit of the quantity recorded in the pixelation graph.
    type (str): Type of quantity to be handled in the graph.
    color (str): Display color of the pixel in the pixelation graph.
    timezone (str): Timezone for this graph as TZ database name.
    is_secret (bool): Whether this graph should be kept secret or not.

    Returns:
    dict: API response.
    """
    url = f"{base_url}/{username}/graphs"

    headers = {
        'Content-Type': 'application/json',
        "X-USER-TOKEN": token,
    }

    # Define the payload
    payload = {
        'id': graph_id,
        'name': graph_name,
        'unit': unit,
        'type': type,
        'color': color,
        'timezone': timezone,
        'isSecret': is_secret,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json()


# Posting a pixel.

def create_pixel(token, username, graph_id, date, quantity, optional_data):
    """Post a pixel to a graph.

    Args:
    token (str): A token string used to authenticate as a user.
    username (str): User name for this service.
    graph_id (str): ID for identifying the pixelation graph.
    date (str): The date on which the quantity is to be recorded.
    quantity (str): The quantity to be registered on the specified date.
    optional_data (str): Additional information other than quantity.

    Returns:
    dict: API response.
    """
    url = f"{base_url}/{username}/graphs/{graph_id}"

    headers = {
        'Content-Type': 'application/json',
        "X-USER-TOKEN": token,
    }

    # Define the payload
    payload = {
        'date': date,
        'quantity': quantity,
        'optionalData': optional_data,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json()


def delete_pixel(token, username, graph_id, date):
    """Delete a pixel from a graph.

    Args:
    token (str): A token string used to authenticate as a user.
    username (str): User name for this service.
    graph_id (str): ID for identifying the pixelation graph.
    date (str): The date of the pixel to delete.

    Returns:
    dict: API response.
    """
    url = f"{base_url}/{username}/graphs/{graph_id}/{date}"

    headers = {
        'Content-Type': 'application/json',
        "X-USER-TOKEN": token,
    }

    response = requests.delete(url, headers=headers)

    return response.json()

def update_pixel(token, username, graph_id, date, quantity):
    """Update a pixel in a graph.

    Args:
    token (str): A token string used to authenticate as a user.
    username (str): User name for this service.
    graph_id (str): ID for identifying the pixelation graph.
    date (str): The date of the pixel to update.
    quantity (str): The new quantity to be registered on the specified date.

    Returns:
    dict: API response.
    """
    url = f"{base_url}/{username}/graphs/{graph_id}/{date}"

    headers = {
        'Content-Type': 'application/json',
        "X-USER-TOKEN": token,
    }

    # Define the payload
    payload = {
        'quantity': quantity,
    }

    response = requests.put(url, headers=headers, data=json.dumps(payload))

    return response.json()

    
# Create a new user
# Replace '<api-token>' and '<username>' with your actual API token and username
user = create_user(
    token="<api-token>",  # Your API token
    username="<username>",  # Your username
    agree_terms_of_service="yes",
    not_minor="yes",
    thanks_code="I appreciate the work that has been put in to develop this api, and love using it!"
)
print(user)

# Create a new graph
# Replace '<api-token>', '<username>', '<graph-id>', and '<timezone>' with your actual information
response = create_graph(
    token="<api-token>",  # Your API token
    username="<username>",  # Your username
    graph_id="<graph-id>",  # The ID for the graph. This will also define the theme of the graph.
    graph_name="Coding-Hours",
    unit="hours",
    type="int",
    color="sora",
    timezone="<timezone>",  # Your timezone, e.g., "Europe/Amsterdam"
    is_secret=True
)
print(response)

# Create a new pixel
# Replace '<api-token>', '<username>', and '<graph-id>' with your actual information
pixel = create_pixel(
    token="<api-token>",  # Your API token
    username="<username>",  # Your username
    graph_id="<graph-id>",  # The ID for the graph. This should match the graph_id used in create_graph
    date=current_date,
    quantity="3",
    optional_data="{\"hours\":\"5\"}"
)
print(pixel)

# Delete a pixel
# Replace '<api-token>', '<username>', and '<graph-id>' with your actual information
deleted_pixel = delete_pixel(
    token="<api-token>",  # Your API token
    username="<username>",  # Your username
    graph_id="<graph-id>",  # The ID for the graph. This should match the graph_id used in create_graph
    date=current_date,
)
print(deleted_pixel)

# Update a pixel
# Replace '<api-token>', '<username>', and '<graph-id>' with your actual information
updated_pixel = update_pixel(
    token="<api-token>",  # Your API token
    username="<username>",  # Your username
    graph_id="<graph-id>",  # The ID for the graph. This should match the graph_id used in create_graph
    date=current_date,
    quantity="5"
)
print(updated_pixel)
