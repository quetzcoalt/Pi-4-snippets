import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

x=40
y=38
#led_pin=37

GPIO.setup(x,GPIO.IN)
GPIO.setup(y,GPIO.IN)

try:
	while 1:
		print(GPIO.input(x), GPIO.input(y))
		time.sleep(.2)
except KeyboardInterrupt:
	GPIO.cleanup()
