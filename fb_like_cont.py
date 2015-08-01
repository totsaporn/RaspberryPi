import max7219.led as led
import urllib
import json
import time

while 1:

   #Get Data From Facebook Fanpage
   response = urllib.urlopen(“http://graph.facebook.com/homeofmaker”)
   data = json.loads(response.read())

   #Print Data
   print data[“username”]
   print “Like = ”, data[“likes”]

   #7-segment display
   device = led.sevensegment()
   device.write_number(devicedId=0, value=data[“likes”])

   time.sleep(0.5)