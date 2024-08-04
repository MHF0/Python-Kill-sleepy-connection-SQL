import mysql.connector
from mysql.connector import Error
import time

def kill_sleep_connections_bottom_to_top():
    # List of database configurations
    databases = [
        {
            'host': 'Host',
            'database': 'information_schema',
            'user': 'user',
            'password': 'password'
        }
    ]
    
    connection = None
    cursor = None

    for db in databases:
        try:
            # Establish the database connection
            connection = mysql.connector.connect(
                host=db['host'],
                database=db['database'],
                user=db['user'],
                password=db['password']
            )
            if connection.is_connected():
                cursor = connection.cursor()
                # Query to find all sleep connections
                cursor.execute("SELECT id FROM information_schema.processlist WHERE command = 'Sleep' ORDER BY id DESC;")
                sleep_connections = cursor.fetchall()
                # Generate and execute KILL statements
                for connection_id in sleep_connections:
                    try:
                        kill_query = f"KILL {connection_id[0]}"
                        cursor.execute(kill_query)
                        print(f"Killed connection ID: {connection_id[0]}")
                    except Error as e:
                        print(f"Error killing connection ID {connection_id[0]}: {e}")
                # Commit changes
                connection.commit()
                break  # Exit loop if successful
        except Error as e:
            print(f"Error connecting to database {db['host']}: {e}")
            time.sleep(5)  # Wait before trying the next database
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print(f"MySQL connection to {db['host']} is closed")

if __name__ == "__main__":
    kill_sleep_connections_bottom_to_top()
