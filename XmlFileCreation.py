'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom

doc = minidom.Document()

root = doc.createElement('html')
doc.appendChild(root)

leaf = doc.createElement('head')
script = doc.createElement('script')
leaf.appendChild(script)
style=doc.createElement('style')
leaf.appendChild(style)
root.appendChild(leaf)
leaf = doc.createElement('body')
div=doc.createElement('div')
para=doc.createElement('p')
para.setAttribute("align","center")
para.setAttribute("color","red")
text=doc.createTextNode('Manually Creating HTML File')
para.appendChild(text)
div.appendChild(para)
leaf.appendChild(div)
root.appendChild(leaf)
xml_str = doc.toprettyxml(indent="  ")
with open("Sample.xml", "w") as f:
    f.write(xml_str)