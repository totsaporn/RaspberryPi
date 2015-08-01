import smbus				#Add the smbus library to a Python sketch
import time					#Add the time library to a Python sketch
import httplib, urllib		#Add the httplib, urllib library to a Python sketch

temp_add=0x48				#Temperature sensor address
temp_config_add=0x01		#Temperature sensor configuration address
temp_raw_add=0x00			#Temperature sensor data address

bus=smbus.SMBus(1)			# Force I2C1 
bus.write_byte_data(temp_add,temp_config_add,0x60)		#Temperature sensor address

while True:
    templaw=bus.read_word_data(temp_add,temp_raw_add)  #Read Raw Data 
    templow=(templaw&0xff00)>>8							
    temphigh=templaw&0x00ff
    temp=(((temphigh*256)+templow)>>4)*.0625
    temp=round(temp,2)									#Data float 2 point
    print("Temp = "+str(temp))		
	
	# temp is the data you will be sending to the thingspeak channel for plotting the graph. 
	# You can add more than one channel and plot more graphs
    params = urllib.urlencode({'field1':temp,'key':'YOUR_API_KEY'}) 	# Change your API KEY
		# use your API key generated in the thingspeak channels for the value of 'key'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")  
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
    time.sleep(60)				#Delay 1 minute