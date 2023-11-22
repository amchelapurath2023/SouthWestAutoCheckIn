import psycopg2
import subprocess

db_params = {
    'host': 'localhost',
    'database': 'flight_reservation_data',
    'user': 'postgres',
    'password': 'password'
}

conn = psycopg2.connect(**db_params)

cursor = conn.cursor()

# Replace this query with your actual query
query = "SELECT name, confirmation_code, flight_time FROM your_table WHERE flight_time <= NOW() + INTERVAL '24 hours';"

cursor.execute(query)
records = cursor.fetchall()

for record in records:
    firstname, lastname, confirmation_code, flight_time = record
    subprocess.run(['python3', 'auto.py', firstname, lastname, confirmation_code])
    