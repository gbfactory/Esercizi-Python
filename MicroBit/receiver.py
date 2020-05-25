from microbit import *
import radio
radio.config(group=38)
radio.on()

while True:
    message = radio.receive()
    sleep(100)
    print(message)
