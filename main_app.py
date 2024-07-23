# main.py
from iss_data import iss_position, astronauts_in_space

if __name__ == "__main__":
    print("Fetching ISS Position...")
    iss_position_data = iss_position()
    print("ISS Position Data Inserted:", iss_position_data)

    print("Fetching Astronauts in Space...")
    astronauts_data = astronauts_in_space()
    print("Astronauts Data Inserted:", astronauts_data)
