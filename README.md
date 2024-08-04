# International_Space_Station-tracker

## Overview

This project aims to design and implement a data engineering pipeline that tracks the real-time position of the International Space Station (ISS) using geospatial data and visualizes its trajectory on an interactive 3D map. The project will integrate multiple data sources, process the incoming data stream, and present the ISS’s position in an intuitive, visually compelling format.


## Objectives:

### 1. Data Collection

This project aims to design and implement a data engineering pipeline that tracks the real-time position of the International Space Station (ISS) using geospatial da
* Stream real-time geospatial data from the ISS, including latitude, longitude, altitude, and velocity.
* Collect additional metadata about the ISS, such as timestamps and orbital parameters.
### 2. Data Processing

* Implemented ETL (Extract, Transform, Load) processes to clean, transform, and enrich the geospatial data.
* Stored the processed data in a database for historical analysis and querying.
* Ensured data integrity and consistency across the pipeline.

### 3. Data Storage

* Utilized MySQL to store geospatial data.
* Implemented efficient indexing and querying mechanisms for real-time data retrieval.
  
### 4. Visualization

* Developed a web-based dashboard using Dash Plotly to visualize the ISS's position on a 3D map.
* Implement features like real-time updates and interactive controls for users to explore the data.
* Provide additional layers of information, such as world map overlays, current position relative to ground stations, and orbital path predictions.



### Technologies & Tools
* Data Collection: APIs (NASA's Open APIs, ISS Tracker APIs)
* Data Processing: Python, Pandas
* Data Storage: MySQL
* Visualization: Dash, Plotly
* Deployment and Automation: Docker, GitHub for version control, Bash shell

### Expected Outcomes
* A robust and scalable data pipeline that accurately tracks and stores the ISS's geospatial data in real time.
* An interactive 3D map visualization that allows users to view the current position of the ISS and gain insights into its orbit.
* A comprehensive documentation of the data pipeline, including setup, deployment, and usage instructions.

### Potential Extensions
* Integration of machine learning models to predict future positions of the ISS.
* Incorporating additional geospatial data sources, such as weather or space debris tracking.
* Extending the visualization to include other satellites or space objects.
