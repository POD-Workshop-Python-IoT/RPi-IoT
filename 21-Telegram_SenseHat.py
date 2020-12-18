import time
import random
import datetime

from sense_hat import SenseHat

import telepot
from telepot.loop import MessageLoop

token = '*** Authorised Token ***'

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    if command == '/roll':
        msg = "Threw a {}".format(random.randint(1,6))
    elif command == '/time':
        msg = "Now is {}".format(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    elif command == '/press':
        msg = "Barometer Pressure = {0:.3f} millibars".format(pressure)
    elif command == '/temp':
        msg = "Temperature = {0:.3f} degC".format(temp)
    elif command == '/humid':
        msg = "Humidity = {0:.3f} %".format(humidity)
    elif command == '/led':
        msg = "Change colour on led"
        sense.clear(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    else:
        msg = "Sorry, I do not know how to do this yet!"
        sense.clear()
        
    bot.sendMessage(chat_id, msg)

bot = telepot.Bot()

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')
sense = SenseHat()

while 1:
    time.sleep(10)