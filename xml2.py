import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="5">
      <id>001</id>
      <name>satvik</name>
    </user>
    <user x="9">
      <id>009</id>
      <name>Ben</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
