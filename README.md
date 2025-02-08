# Plane / wheater balloon api
This is an simple api that i plan to use for long range plane missions and for a wheater balloon that will have an lte module attached to them.
this will allow me to monitor its position through the api and ill also be able to see a log of positions and if an fpv camera is attached you can send images to make it easier to recover your craft once landed

# Documentation:

## /get-sensor-data
this lets you get the last uploaded sensor data in json format
this is used with a GET

## /post-sensor-data
this lets you post the sensor data in json format from the craft
it automatically also logs everything it receives to sensor_data.json
this is used with a POST

## /upload
this lets you upload an image called image.png
this is used with a POST

## /download
this lets you download the uploaded image.
this is used with a GET

## /get-log
this returns the entire log in json format
this is used with a GET

## /clear-log
this clears the entire log
this is used with a DELETE

### details:
when you create sensor_data.json make sure that it already has 
{}
inside or else the api might error when it tries to write a new entry



