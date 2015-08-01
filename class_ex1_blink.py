import RPi.GPIO as GPIO			#Add the GPIO library to a Python sketch
import time						#Add the time library to a Python sketch

GPIO.setmode(GPIO.BOARD)		#Setup GPIO using Board numbering
GPIO.setup(8, GPIO.OUT)			#Setup pin 8 to output

while True:
	GPIO.output(8,GPIO.HIGH)	#Set LED pin 8 to HIGH
	time.sleep(1)				#Delay 1 second
	GPIO.output(8,GPIO.LOW)		#Set LED pin 8 to LOW
	time.sleep(1)				#Delay 1 second