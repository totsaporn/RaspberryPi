import max7219.led as led
import urllib2
import json
import time

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason
			
			
			
while 1:
	page_id = "220577814776434" # username or id Sathittham.com
	token = "CAAUPwb9lSv0BALCKWiHlobvLZBZAiQN8OntZBbrQAaxVFufGTl8qqUvpPgaE83ZCFoSLl5WbDhoRvt3bSxZBW2Y8HpP5lnS8XRRrOysJFOF5UBnh9beIRcWoLTib3LgBaHqQCUrC2UFrT1nay5NTrS5UWZCZCFQolBBLBH3Mea26qTzScTPu1Gy6MQ4NUxtPuD4ZCf7bjxoO9ZBNPbPBBZBJe5"  # Access Token
	page_data = get_page_data(page_id,token)

	print "Page Name:"+ page_data['name']
	print "Likes:"+ str(page_data['likes'])
	print "Link:"+ page_data['link']


	#7-segment display
    device = led.sevensegment()
    device.write_number(deviceId=0, value=page_data['likes'])

    time.sleep(0.5)