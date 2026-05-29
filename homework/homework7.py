import RPi.GPIO as GPIO
import time

in_pin=40
out_pin=38

GPIO.setmode(GPIO.BOARD)

GPIO.setup(in_pin,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(out_pin,GPIO.OUT)

clicked=0
curr=1
prev=1

try:
	while True:
		curr=GPIO.input(in_pin)
		if curr==1 and prev==0:
			clicked = not clicked
			GPIO.output(out_pin,clicked)
		prev=curr
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Bye.")
