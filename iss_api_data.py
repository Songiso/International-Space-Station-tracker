# iss_data.py
import urllib.request
import json
from database_iss import insert_iss_position, insert_astronaut

def iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    # Extracting the necessary information
    timestamp = result["timestamp"]
    latitude = result['iss_position']['latitude']
    longitude = result['iss_position']['longitude']
    
    # Insert data into the database
    insert_iss_position(timestamp, latitude, longitude)

    # Creating the dictionary
    position_data = {
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude
    }

    return position_data


def astronauts_in_space():
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    astronauts = []
    for person in result['people']:
        name = person['name']
        craft = person['craft']
        insert_astronaut(name, craft)
        astronauts.append({'name': name, 'craft': craft})
    
    return astronauts
