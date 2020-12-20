from urllib.request import urlopen, Request
import json,time

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    request = Request('https://api.thingspeak.com/talkbacks/41122/commands/execute?api_key=4E2U6B7VRBGIOE6D')
    response = urlopen(request)
    command = response.read()
    command = command.decode()
    command = command
    if len(command) > 0:
        print(command)

    if command == 'LED_ON':
        sense.clear(255,255,255)
    if command == 'LED_OFF':
        sense.clear()
    time.sleep(5)  