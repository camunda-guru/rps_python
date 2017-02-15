'''
Created on 14-Feb-2017

@author: BALASUBRAMANIAM
'''
from Fidelity_Day1 import *
import sys
status=None
y=12
x=30
try:
    password=input('Enter Password')
    #number=x/y
    if(len(password)>=4 and len(password)<=8):
        print("Accepted")
    else:
        raise Exception('Length not sufficient')
except Exception as e:
    print(e)
finally:
    print("Finally all connections closed")

