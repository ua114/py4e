# Using XML

# import xml.etree.ElementTree as ET
#
# data = '''
# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#     +1 734 303 4456
#   </phone>
#   <email hide="yes" />
# </person>'''
#
# tree = ET.fromstring(data)
# print(tree)
# print(tree.find('name').text)
# print('Phone:',tree.find('phone').text)
# print('Email:',tree.find('email').get('hide'))

# XML multiple trees

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)

lst = stuff.findall('users/user')
print(lst)
print('User count:', len(lst))

lst2 = stuff.findall('user')
print('User count:', len(lst2))
