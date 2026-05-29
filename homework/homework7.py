import RPi.GPIO as GPIO
import time

in_pin=40
out_pin=38

GPIO.setmode(GPIO.BOARD)

GPIO.setup(in_pin,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(out_pin,GPIO.OUT)

clicked = False

try:
	while True:
		in_value=GPIO.input(in_pin)
		# print(in_value)
		if in_value == 0:
			clicked = not clicked
			print(in_value)
			time.sleep(0.2)

		GPIO.output(out_pin,clicked)
except KeyboardInterrupt:
	GPIO.cleanup()

