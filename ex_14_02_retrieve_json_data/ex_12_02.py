import json
import urllib.request

url = input('enter a url:')
if len(url) <1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
#use read() method to transform HTTP response object (for which we have to use for in to go through its elements) into string delimited with endlines characters \n and byte objects in utf-8:
data = urllib.request.urlopen(url).read()
# we have to transform byte objects into proper string
#data = fhand.decode()
#print(data) ->string unicode

#transform the string into a readable dict/list of data
info=json.loads(data)
print(json.dumps(info))
#print(info)
#print(info['comments'])
sum=0
for comment in info['comments']:
    sum = sum + comment['count']
print(sum)
    
    
