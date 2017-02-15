'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
import os
from xml.dom import minidom
os.chdir('G:\Local Disk\Python')
'''
doc=minidom.parse("CountryData.xml")
table = doc.getElementsByTagName("Table")
for nodeData in table:
    data = nodeData.getElementsByTagName("Country")
    for c1 in data:
       print(c1.firstChild.data)
    
    data = nodeData.getElementsByTagName("City")
    for c2 in data:
       print(c2.firstChild.data)
'''

import xml.etree.ElementTree as ET
tree = ET.parse('CountryData.xml')
root = tree.getroot()
for child in root:
   print (child.tag, child.attrib)
  
for tabref in root.findall('Table'):
    country = tabref.find('Country').text
    city = tabref.find('City').text
    print (country, city)
    
newNode = ET.Element('newTableNode')
root.insert(3, newNode) 
 
for child in root:
   print (child.tag, child.attrib)
   




    
    
