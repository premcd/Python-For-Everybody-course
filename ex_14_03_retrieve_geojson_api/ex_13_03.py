import json, ssl
import urllib.request, urllib.parse

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('enter an address:')
api_url = 'http://py4e-data.dr-chuck.net/opengeo?'

address = address.strip()
print(address)
parms = dict()
parms['q'] = address
url_to_send = api_url + urllib.parse.urlencode(parms)
print('retrieving', url_to_send)

data = urllib.request.urlopen(url_to_send).read()
info = json.loads(data.decode())
print(info)
print(json.dumps(info, indent=4))
print('code for this address is:',info['features'][0]['properties']['plus_code'])

