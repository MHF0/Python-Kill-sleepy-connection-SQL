# Kill Sleep Connections

## Overview

This Python script is designed to manage idle (sleep) connections in MySQL databases. It connects to a specified list of MySQL databases and terminates sleep connections in reverse order (bottom to top). This can help optimize database performance by freeing up resources used by inactive connections.

## Features

- Connects to MySQL databases using provided configurations.
- Identifies and kills idle sleep connections.
- Processes connections from bottom to top (by connection ID).
- Handles multiple databases in sequence.
- Includes error handling and connection management.

## Requirements

- Python 3.x
- `mysql-connector-python` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required MySQL connector library:
   ```bash
   pip install mysql-connector-python
   ```

## Usage

1. Update the `databases` list in the script with your MySQL database configurations.
2. Run the script:
   ```bash
   python kill_sleep_connections.py
   ```

## Script Details

The script performs the following steps:

1. Defines a list of database configurations.
2. Iterates over the list to connect to each database.
3. Executes a query to find sleep connections, ordered by ID in descending order.
4. Generates and executes `KILL` statements for each idle connection.
5. Handles errors and closes database connections appropriately.

## Error Handling

The script includes basic error handling for connection failures and issues while killing connections. It logs errors and waits before attempting to connect to the next database.

## License

This script is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Please submit issues or pull requests to the GitHub repository.
