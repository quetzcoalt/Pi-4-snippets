import RPi.GPIO as GPIO
import time

ON=1
OFF=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

play = True

while play:
	blinks = int(input("How many times do you want to blink the LED? "))
	delay = float(input("How much time between each blink? "))

	for i in range(blinks):
		GPIO.output(11,ON)
		time.sleep(1)
		GPIO.output(11,OFF)
		time.sleep(delay)

	again = int(input("Try again? press 1 if yes, press 0 if no. "))

	if not again:
		play = False
		print("Bye Bye.")

GPIO.cleanup()
