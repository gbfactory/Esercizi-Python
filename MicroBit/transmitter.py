from microbit import *
import radio
radio.config(group=38)
radio.on()

while True:
    sleep(30)
    radio.send(str(accelerometer.get_values()))
