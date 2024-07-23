# database.py
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        user='root', 
        password='yourpassword', 
        host='yourhost', 
        database='yourdatabase'
    )

def insert_iss_position(timestamp, latitude, longitude):
    conn = connect_db()
    cursor = conn.cursor()
    insert_query = "INSERT INTO iss_position (timestamp, latitude, longitude) VALUES (%s, %s, %s)"
    cursor.execu# database.py
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        user='yourusername', 
        password='yourpassword', 
        host='yourhost', 
        database='yourdatabase'
    )

def insert_iss_position(timestamp, latitude, longitude):
    conn = connect_db()
    cursor = conn.cursor()
    insert_query = "INSERT INTO iss_position (timestamp, latitude, longitude) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (timestamp, latitude, longitude))
    conn.commit()
    cursor.close()
    conn.close()

def insert_astronaut(name, craft):
    conn = connect_db()
    cursor = conn.cursor()
    insert_query = "INSERT INTO astronauts_in_space (name, craft) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, craft))
    conn.commit()
    cursor.close()
    conn.close()
te(insert_query, (timestamp, latitude, longitude))
    conn.commit()
    cursor.close()
    conn.close()

def insert_astronaut(name, craft):
    conn = connect_db()
    cursor = conn.cursor()
    insert_query = "INSERT INTO astronauts_in_space (name, craft) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, craft))
    conn.commit()
    cursor.close()
    conn.close()
