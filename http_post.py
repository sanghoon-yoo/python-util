import urllib.request
import urllib.parse
import json
import urllib
import base64



data = json.loads('{"grant":"credentials","type":"USER"}')
secret = "secret_key"
encoded_bytes = base64.b64encode(secret.encode('utf-8'))
encoded_string = encoded_bytes.decode('utf-8')

postdata = urllib.parse.urlencode(data).encode("UTF-8")
urlpath = urllib.request.Request('https://test.com/oauth/token', postdata, headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic '+encoded_string})
resource = urllib.request.urlopen(urlpath)
responsedata = resource.read().decode(resource.headers.get_content_charset())
print(responsedata)





#python 2.7
'''
import urllib
import urllib2
import json
import base64

data = json.loads('{"grant":"credentials","type":"USER"}')
secret = "secret_key"
encoded_string = base64.b64encode(secret)

postdata = urllib.urlencode(data)
urlpath = urllib2.Request('https://test.com/oauth/token', postdata, headers={'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic ' + encoded_string})
resource = urllib2.urlopen(urlpath)
responsedata = resource.read().decode(resource.headers.getheader('Content-Type').split('charset=')[-1])
print(responsedata)
'''
