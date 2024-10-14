import time
import requests
import serial

# Establish serial communication with micro:bit; replace with your serial port
# Note: 115200 is the baud rate for micro:bit
ser = serial.Serial('COM5', 115200)  # Set a timeout for reading

# API URL for updating ThingSpeak channel
url = "https://api.thingspeak.com/update.json"
api_key = 'I5LET0G5ZQPWK7HZ'  # Replace with your API key for the new lab8_2 channel

# Continuously read data from micro:bit
time_interval = None
light = None
while True:
    try:
        # Read line from micro:bit
        mbit_data = ser.readline().decode('utf-8').strip()  # Convert bytes to string and strip whitespace
        print(f"Raw data from micro:bit: {mbit_data}")  # Debug output

        # Initialize variables for time interval and light level
   
        
        # Check if the line contains temperature and light values
        if  'time_interval' in mbit_data :
            time_interval = mbit_data.split(":")[1]
        elif 'light' in mbit_data:
            light = mbit_data.split(":")[1]

        print(light, mbit_data.split(':'), time_interval)
        
        # Ensure both values have been captured
        if time_interval is not None and  light is not None:
            # Prepare API call for ThingSpeak with time and light data
            datastring = {'api_key': api_key, 'field1': time_interval, 'field2': light}
            response = requests.post(url, data=datastring)
            print(f"Sent data {datastring} to {url}, got status code {response.status_code}")

            # Append time, light data, and timestamp to index.html
            with open("lab83/index.html", "a") as indexfile:
                indexfile.write(f'<tr><td>{time_interval}</td><td>{light}</td><td>{time.ctime()}</td></tr>\n')
        
        time.sleep(1)  # Add a delay to avoid overwhelming the ThingSpeak API

    except Exception as e:
        print(f"Error: {e}")
