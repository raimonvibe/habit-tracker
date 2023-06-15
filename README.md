# Pixela Python Tracker

This repository contains Python scripts that interact with the Pixela API, a habit tracking and visualization service. With this script, you can automate tracking your habits or activities and visualize them in the form of a GitHub-like graph.

## My own link to the project:

https://pixe.la/v1/users/raimoncoding/graphs/coding-hours.html

## Dependencies

- Python 3.x
- `requests` library

## Setup

1. Clone this repository.
2. Install dependencies using pip: `pip install requests`
3. Replace `<api-token>`, `<username>`, `<graph-id>`, and `<timezone>` with your actual information in the script.

## Usage

Run the main script:

python pixela_tracker.py

## Functions
The following functions are included in the script:

create_user(token, username, agree_terms_of_service, not_minor, thanks_code): Creates a new user.
create_graph(token, username, graph_id, graph_name, unit, type, color, timezone, is_secret): Creates a new graph.
create_pixel(token, username, graph_id, date, quantity, optional_data): Posts a pixel to a graph.
delete_pixel(token, username, graph_id, date): Deletes a pixel from a graph.
update_pixel(token, username, graph_id, date, quantity): Updates a pixel in a graph.
Each function corresponds to a specific action you can take via the Pixela API, and all parameters are necessary for the API request. Ensure to replace placeholder values with actual data before running the script.

## Contributing
Contributions are always welcome. Please make sure to update tests as appropriate.

## License
This project is licensed under the MIT License.

https://github.com/raimoncoding/habit-tracker/blob/main/LICENSE.txt

For more details, please refer to the license file in the repository.

