import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

in_pin=40
out_pin=38

GPIO.setup(in_pin,GPIO.IN)
GPIO.setup(out_pin,GPIO.OUT)

try:
	while True:
		in_value=GPIO.input(in_pin)
		if in_value == 0:
			GPIO.output(out_pin,1)
		else:
			GPIO.output(out_pin,0)
except KeyboardInterrupt:
	GPIO.cleanup()
