from sense_hat import SenseHat
import httplib
import urllib
import time

def update_sense_data():
     #Read SenseHat sensor data
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    #initial to show example of reading one sensor data??
    #params = urllib.urlencode({'field1': temp, 'key':key })
    params1 = urllib.urlencode({'field1': temp, 'field2': humidity, 'field3': pressure, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")

    try:
        #conn.request("POST", "/update", params, headers)
        conn.request("POST", "/update", params1, headers)
        response = conn.getresponse()
        print("Temperature is %f" %temp)
        print("Humidity is %f" %humidity)
        print("Pressure is %f" %pressure)
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")

#Initial setup
sense = SenseHat()
sense.clear()
key = "*** Authorised Key ***"  # Put your API Key here
  
#Test resding of SenseHat data
temp = sense.get_temperature()
print("Current Temperature is %f" %temp)
humidity = sense.get_humidity()
print("Current Humidity is %f" %humidity)
pressure = sense.get_pressure()
print("Current Pressure is %f" %pressure)
print("\n\n")

#Loop to reand and send data continuously
while True:
    update_sense_data()
    time.sleep(15)
