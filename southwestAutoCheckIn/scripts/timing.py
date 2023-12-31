import psycopg2
import subprocess

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
            select_query = 'SELECT id, first_name, last_name, confirmation_code, flight_time, phone_number FROM "southwestAutoCheckIn_flightreservation" WHERE flight_time <= NOW() + INTERVAL \'24 hours\';'
            cursor.execute(select_query)
            records = cursor.fetchall()


            for record in records:
                record_id, first_name, last_name, confirmation_code, flight_time, phone_number = record
                subprocess.run(['python3', '/Users/anshul/projects/southwestAutoCheckIn/scripts/auto.py', confirmation_code, first_name, last_name, phone_number])


                delete_query = f'DELETE FROM "southwestAutoCheckIn_flightreservation" WHERE id = {record_id};'
                cursor.execute(delete_query)



            conn.commit()

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    check_flight_reservations()
