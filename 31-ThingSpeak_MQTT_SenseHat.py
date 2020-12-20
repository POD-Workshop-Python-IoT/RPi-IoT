from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import time

from sense_hat import SenseHat

string.alphanum = '1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1264630"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "2GOYJVFF6B82UZI5"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "ict_pod"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "2ND90CMWBXDRJQ9B"

tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

sense = SenseHat()
sense.clear()

while(1):

    clientID = ''

    # Create a random clientID.
    for x in range(1,16):
        clientID += random.choice(string.alphanum)

    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    # build the payload string.
    payload = "field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(pressure)

    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
        print (" Published TEMPERATURE = ",temperature," HUMIDITY = ", humidity," PRESSURE = ", pressure," to host: " , mqttHost , " clientID= " , clientID)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")
        
    time.sleep(30)
