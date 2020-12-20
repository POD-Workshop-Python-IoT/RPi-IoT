import sys
import urllib3
from time import sleep

from sense_hat import SenseHat

# Enter Your API key here
myAPI = '*** Authorisation Key ***' 

# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

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

    # If reading is valid
    if isinstance(temp, float) and isinstance(humid, float) and isinstance(press, float):
        
        # Formatting to two decimal places for display
        print("Temperature = {:.2f}, Humidity = {:.2f}, Pressure = {:.2f}".format(temp,humid,press))

        try:
            http = urllib3.PoolManager()
            
            # Sending the data to thingspeak
            r = http.request('GET', baseURL + '&field1=%s&field2=%s&field3=%s' % (temp, humid, press))
            print(r.status)
    
        except:
            print('Break..')
            break
    else:
        print('Error')
        break
    
    sleep(15)
