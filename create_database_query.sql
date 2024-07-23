-- Create the database
CREATE DATABASE IF NOT EXISTS iss_tracking;

-- Use the created database
USE iss_tracking;

-- Create the iss_position table
CREATE TABLE IF NOT EXISTS iss_position (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp BIGINT NOT NULL,
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the astronauts_in_space table
CREATE TABLE IF NOT EXISTS astronauts_in_space (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    craft VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
