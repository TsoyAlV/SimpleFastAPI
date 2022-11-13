import psycopg2

HOST_DB = 'localhost'
PORT = 5432
POSTGRES_USER='admin'
POSTGRES_PASSWORD="admin"
POSTGRES_DB='rainbow_database'

conn = psycopg2.connect(host=HOST_DB, port=PORT, database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
cur = conn.cursor()
cur.execute("CREATE TABLE phonebook2 ( user_id serial PRIMARY KEY, firstname VARCHAR ( 255 ) NOT NULL, lastname VARCHAR ( 255 ) NOT NULL, phone_number VARCHAR ( 255 ) NOT NULL, age INT)")
conn.commit()
conn.close()
cur.close()

