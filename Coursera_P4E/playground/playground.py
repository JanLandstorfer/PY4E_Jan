import xml.etree.ElementTree as ET
data = '''<person>
    <name>Jan</name>
    <phone type="intl">
        +4917643240898
     </phone>
     <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))
