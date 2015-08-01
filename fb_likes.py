import urllib2
import json

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

page_id = "1607672509519083" # username or id
token = "CAAW2K2zYVOsBAHBfqbqlyH02DHNapXWtMwmfKo9dJQqinJVWUicyLPoZCOuaf0iMQzcJMZAcHnWfHJZCn3YpBxKNpLGXZBGa8HtpgAhVfcbPTrSUfI2JiDqj2ngi5EhXvWPVaskrZBT5RiDtVeZAWsASMqHQ6EuUmlLTnw6BHMdEUKvu9VpVIpBZBKfxgbxlavYMFyLoYy4RdjuCqVy83ZCuE6GVYQbcRvCTjcafM9E9kwZDZD"  # Access Token
page_data = get_page_data(page_id,token)

print "Page Name:"+ page_data['name']
print "Likes:"+ str(page_data['likes'])
print "Link:"+ page_data['link']