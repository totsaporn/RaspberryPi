import RPi.GPIO as GPIO	#Add the GPIO library to a Python sketch
import time		#Add the time library to a Python sketch

def clearLED():
	GPIO.output(8,GPIO.LOW)		#Set LED pin 8 to LOW	
	GPIO.output(10,GPIO. LOW)	#Set LED pin 10 to LOW	
	GPIO.output(12,GPIO. LOW)	#Set LED pin 12 to LOW	
	GPIO.output(16,GPIO. LOW)	#Set LED pin 16 to LOW	

pin=[8,10,12,16]				#Number of LED pin
counter=0
GPIO.setmode(GPIO.BOARD)		#Setup GPIO using Board numbering

for i in range(0,4):
	GPIO.setup(pin[i], GPIO.OUT)#Setup pin 8,10,12,16 to output

while True:
	clearLED()
	GPIO.output(pin[counter],GPIO.HIGH)	#Set LED to HIGH	
	time.sleep(1)			#Delay 1 second
	counter=counter+1
	if (counter>3):
		counter=0
