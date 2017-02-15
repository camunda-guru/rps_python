'''
Created on 14-Feb-2017

@author: BALASUBRAMANIAM
'''
from pip._vendor.distlib.compat import raw_input
import sys
months=0
 
     
basicSalary = raw_input('Enter Salary')
da=raw_input('Enter DA')
CTC = (int(basicSalary)+int(da))*12
NetSalary=CTC/months
print("CTC","\t",CTC)
print("Net Salary","\t",NetSalary)

    
list=[4367,4389,7808707]
for _ in list:
    print(_)

