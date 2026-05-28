import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

LOW=0
HIGH=1

def pin_state(a, b, c, d, e):
	GPIO.output(29,a)
	GPIO.output(31,b)
	GPIO.output(33,c)
	GPIO.output(35,d)
	GPIO.output(37,e)

def dec_bin(n):
	res = ''
	while n > 0:
		res = str(n & 1) + res
		n >>= 1
	return res.rjust(5,"0")

for i in range(32):
	count = dec_bin(i)
	pin_state(int(count[0]), int(count[1]), int(count[2]), int(count[3]), int(count[4]))
	time.sleep(0.2)

GPIO.cleanup()

