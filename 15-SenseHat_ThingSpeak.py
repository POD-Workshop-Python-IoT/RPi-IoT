from sense_hat import SenseHat
import thingspeak
import json
import time

channel_id = ****** # PUT CHANNEL ID HERE
write_key  = '****************' # PUT YOUR API KEY HERE
read_key   = '****************' # PUT YOUR API KEY HERE

def read(channel):
    try:
        read = channel.get_field_last(field='field1')
        print("Read:", read)
        data = json.loads(read)
        print(data['field1'])  # temperature

        read = channel.get_field_last(field='field2')
        print("Read:", read)
        data = json.loads(read)
        print(data['field2'])  # humidity
        
        read = channel.get_field_last(field='field3')
        print("Read:", read)
        data = json.loads(read)
        print(data['field3'])  # pressure

    except:
        print("connection failed")
    

def update(channel):
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    
    try:
        # write
        response = channel.update({'field1': temperature, 'field2': humidity, 'field3': pressure})

    except:
        print("connection failed")

sense = SenseHat()
sense.clear()

while True:
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    update(channel)

    time.sleep(15)

    channel = thingspeak.Channel(id=channel_id, api_key=read_key)
    read(channel)

    time.sleep(15)
    # free account has an api limit of 15sec
