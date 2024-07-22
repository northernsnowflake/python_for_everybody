import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        + 734 303 4456
        </phone>
        <email hide ="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text) # find me the name, but only text of it (tree)
print('Attr:', tree.find('email').get('hide')) #gp ding mr the email, and from it only itś arribute hude. There is no text