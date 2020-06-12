import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = ' http://py4e-data.dr-chuck.net/comments_517458.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', len(counts))

s = 0
for item in counts:
     s += int(item.text)
     #print('count', item.text)
print('Sum:', s)