import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

try:
	while 1:
		GPIO.output(37,1)
except KeyboardInterrupt:
	GPIO.cleanup()
