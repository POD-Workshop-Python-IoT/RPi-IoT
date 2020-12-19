import sys
import urllib2
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
	try:
		temp, humid, press = sensehat_data()
		
    # If Reading is valid
		if isinstance(temp, float) and isinstance(humid, float) and isinstance(press, float):
			# Formatting to two decimal places
			temp = '%.2f' % temp
			humid = '%.2f' % humid
      press = '%.2f' % press
      
			# Sending the data to thingspeak
			conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (temp, humid, press))
			print conn.read()
			
      # Closing the connection
			conn.close()
		else:
			print 'Error'
      
		sleep(20)
	except:
		break
    
