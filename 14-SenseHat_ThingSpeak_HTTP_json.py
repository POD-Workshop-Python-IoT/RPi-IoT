from sense_hat import SenseHat
import requests
from time import sleep

# Enter Your API key here
myAPI = '*** Authorised Token ***' 

# URL where we will send the data, Don't change it
URL = 'https://api.thingspeak.com/update.json'

def sensehat_data():
    # Reading from SenseHat and storing the temperature, humidity & pressure
    temperature = sense.get_temperature()
    humidity = sense.get_humidity() 
    pressure = sense.get_pressure() 
    return temperature, humidity, pressure

# initialization
sense = SenseHat()
sense.clear()

while True:
    
    temp, humid, press = sensehat_data()
    # Formatting to two decimal places for display
    print("Temperature = {:.2f}, Humidity = {:.2f}, Pressure = {:.2f}".format(temp,humid,press))

    # If reading is valid
    if isinstance(temp, float) and isinstance(humid, float) and isinstance(press, float):
        
        jsonData = '{"api_key":"%s","field1":%f,"field2":%f,"field3":%f}' % (myAPI, temp, humid, press)
        print(jsonData)

        header = {"Content-Type": "application/json","Accept": "text/plain"} 
        
        try:
            # Sending the data to thingspeak
            response = requests.post(url=URL, data = jsonData, headers = header)
            print(response)
    
        except Exception as e:
            print('Break..')
            print(e)
            break
    else:
        print('Error')
        break
    
    sleep(15)
