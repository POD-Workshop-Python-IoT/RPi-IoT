# Install Telegram and then obtain authorisation token from BotFather
# see https://core.telegram.org/bots

import time
import random
import datetime

import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/roll':
        msg = "Threw a {}".format(random.randint(1,6))
    elif command == '/time':
        msg = "Now is {}".format(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    else:
        msg = "Sorry, I do not know how to do this yet!"
        
    bot.sendMessage(chat_id, msg)

bot = telepot.Bot('*** Authorised Token ***')

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
