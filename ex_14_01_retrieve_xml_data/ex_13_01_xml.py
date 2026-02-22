import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input('enter a url:')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
data = urllib.request.urlopen(url).read()
print('retrieve:',len(data),'characters')
#for line in data:
#   print(line.decode().strip())
tree = ET.fromstring(data)
#print(tree)
counts =tree.findall('comments/comment/count')
sum = 0
for c in counts:
    print(c.text)
    sum = sum + int(c.text)
print(sum)
 
