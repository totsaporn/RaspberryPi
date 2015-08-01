import RPi.GPIO as GPIO				#Add the GPIO library to a Python sketch

GPIO.setmode(GPIO.BOARD)			#Setup GPIO using Board numbering
GPIO.setup(8, GPIO.OUT)				#Setup pin 8 to output
GPIO.setup(7, GPIO.IN)				#Setup pin 7 to input

while True:
	if (GPIO.input(7)==1):			#Read Botton pin 7
		GPIO.output(8,GPIO.HIGH)	#Set LED pin 8 to HIGH
 	else:
		GPIO.output(8,GPIO.LOW)		#Set LED pin 8 to LOW