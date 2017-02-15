'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
import os
from _sqlite3 import Row

pathname='G:\Local Disk\Python\SampleData'
os.chdir(pathname)
file=open('ProductInfo.csv',mode='r')

for row in file:
   #print(row)
   colArray = row.split(',')
   for col in colArray:
     print(col)    
    
  

