import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

dim_pin=40
light_pin=38
led_pin=37

GPIO.setup(dim_pin,GPIO.IN)
GPIO.setup(light_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

frequency=100
dc=50 # duty cycle
min_dc=0
max_dc=100

pwm=GPIO.PWM(led_pin,frequency)
pwm.start(dc)

dim_curr=0
dim_prev=0

light_curr=0
light_prev=0

try:
	while 1:
		print(dim_curr,light_curr)

		dim_curr=GPIO.input(dim_pin)
		light_curr=GPIO.input(light_pin)

		if dim_curr==1 and dim_prev==0:
			dc=max(min_dc,dc-5)
		if light_curr==1 and light_prev==0:
			dc=min(max_dc,dc+5)
		pwm.ChangeDutyCycle(dc)
		dim_prev=dim_curr
		light_prev=light_curr
		time.sleep(0.2)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
