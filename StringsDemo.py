'''
Created on 13-Feb-2017

@author: BALASUBRAMANIAM
'''
from django.template.defaultfilters import first

message='welcome'
print(message)
message="Welcome to training\
            in Ramunjam IT City Chennai"
            
message='''Welcome to training in Ramunjam IT City Chennai,"Learning python is fun"'''
print(message)

path=r'g:\table'
message='http://www.google.com'
print(message[-6:len(message)])
firstname='fidelity investments'
print(firstname.capitalize())
print(firstname.upper())
name='TIDEL Park'
print(name.casefold())
amount='4728587458258'
print(amount.center(len(amount)+10,'*'))

phone="454*678*68767-6787"
#result= phone.split("*")
result = phone.split(sep='-',maxsplit=1)
print(result[0].split('*'),result[1])





