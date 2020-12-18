from sense_hat import SenseHat
import time
import random
import datetime
import thingspeak
import telepot
from telepot.loop import MessageLoop

channel_id = ****** # PUT CHANNEL ID HERE
write_key  = '****************' # PUT YOUR API KEY HERE
bot_token = '*** Authorised Token ***'

def update(channel):
    try:
        # write
        response = channel.update({'field1': temperature, 'field2': humidity, 'field3': pressure})
        
        print("Temperature = {0:.3f} degC".format(temperature))
        print("Humidity = {0:.3f} %".format(humidity))
        print("Barometer Pressure = {0:.3f} millibars".format(pressure))

    except:
        print("connection failed")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    pressure = sense.get_pressure()
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()

    if command == '/roll':
        msg = "Threw a {}".format(random.randint(1,6))
    elif command == '/time':
        msg = "Now is {}".format(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    elif command == '/press':
        msg = "Barometer Pressure = {0:.3f} millibars".format(pressure)
    elif command == '/temp':
        msg = "Temperature = {0:.3f} degC".format(temperature)
    elif command == '/humid':
        msg = "Humidity = {0:.3f} %".format(humidity)
    elif command == '/led':
        msg = "Change colour on led"
        sense.clear(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    else:
        msg = "Sorry, I do not know how to do this yet!"
        sense.clear()
        
    bot.sendMessage(chat_id, msg)
    measure(channel)

bot = telepot.Bot(token)

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

sense = SenseHat()
channel = thingspeak.Channel(id=channel_id, api_key=write_key)

while True:
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    
    update(channel)
   
    # free account has an api limit of 15sec
    time.sleep(15)
