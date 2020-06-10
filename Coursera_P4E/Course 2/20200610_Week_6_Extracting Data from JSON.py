import urllib.request, urllib.error
import json


url = 'http://py4e-data.dr-chuck.net/comments_517459.json'
uh = urllib.request.urlopen(url)
data = uh.read()


info = json.loads(data)
print('Retrieved', len(data), 'characters')
print('User count:', len(info['comments']))

s = 0

for item in info['comments']:

    s += int(item['count'])
    # print('Name', item['name'])
    # print('count', item['count'])

print('Sum:', s)
