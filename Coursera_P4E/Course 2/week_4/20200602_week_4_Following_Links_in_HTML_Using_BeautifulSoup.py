# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


position_in = 18
position = position_in - 1
count = 7

url = ' http://py4e-data.dr-chuck.net/known_by_Prisha.html'
first_name = re.search('by_([a-zA-Z]+).html', url).group(1)

names_pp = list()

for i in range (0, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    urllist = list()
    namelist = list()
    tags = soup('a')
    #urls = soup.find_all('a', href=True)

    for tag in tags:
        #print(tag.get('href', None))
        names = (tag.contents[0])
        namelist.append(names)


    html = urllib.request.urlopen(url, context=ctx).read()
    links = re.findall(b'href="(http[s]?://.*?)"', html)

    for link in links:
        urllist.append(link.decode())
        #print(link.decode())
    url = urllist[position]
    names_pp.append(namelist[position])
    #print(namelist[position])
#print(urls[2])

name = ' '.join(names_pp)
print(first_name, name)
