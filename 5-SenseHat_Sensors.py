from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print("Barometer Pressure = {0:.3f} millibars".format(pressure))

temp = sense.get_temperature()
print("Temperature = {0:.3f} degC".format(temp))

humidity = sense.get_humidity()
print("Humidity = {0:.3f} %".format(humidity))