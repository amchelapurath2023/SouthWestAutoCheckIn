import psycopg2
import subprocess
from time import sleep

def check_flight_reservations():
    db_params = {
        'host': 'localhost',
        'database': 'checkindata',
        'user': 'postgres',
        'password': 'password'
    }

    while True:
        try:
            conn = psycopg2.connect(**db_params)
            cursor = conn.cursor()

            # Replace this query with your actual query
            query = "SELECT firstname, lastname, confirmation_code, flight_time, phonenumber FROM southwestAutoCheckIn_flightreservation WHERE flight_time <= NOW() + INTERVAL '24 hours';"
            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                firstname, lastname, confirmation_code, phonenumber = record
                subprocess.run(['python3', 'auto.py', firstname, lastname, confirmation_code, phonenumber])

        except Exception as e:
            print(f"Error: {e}")

        finally:
            if conn:
                conn.close()

        # Sleep for an interval before checking again (e.g., every 5 minutes)
        sleep(300)

if __name__ == "__main__":
    check_flight_reservations()
