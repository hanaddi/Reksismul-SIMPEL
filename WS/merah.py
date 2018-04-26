#/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LampuMerah = 4
GPIO.setup(LampuMerah, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cekMerah() :
	return GPIO.input(LampuMerah)==0

while (True) :
	if cekMerah() :
		print "Mereah"
	else :
		print "---"
	time.sleep(1)

GPIO.cleanup()


