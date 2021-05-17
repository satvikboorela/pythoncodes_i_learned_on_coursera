import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Satvik</name>
  <phone type="intl">
    7346303556
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
