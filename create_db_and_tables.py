# create_db_and_tables.py
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        user='root', 
        password='12345678', 
        host='localhost'
    )

def create_database_and_tables():
    conn = connect_db()
    cursor = conn.cursor()
    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS iss_tracking")

    # Use the created database
    cursor.execute("USE iss_tracking")

    # Create iss_position table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iss_position (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp BIGINT NOT NULL,
        latitude DECIMAL(9, 6) NOT NULL,
        longitude DECIMAL(9, 6) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create astronauts_in_space table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS astronauts_in_space (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        craft VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database_and_tables()
    print("Database and tables created successfully.")
