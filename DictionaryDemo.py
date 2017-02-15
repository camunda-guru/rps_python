'''
Created on 14-Feb-2017

@author: BALASUBRAMANIAM
'''
from datetime import date 
# key pair vlue
customerDB={437956:{'Name':'Anoop','DOB':date(1995,5,5),
                    'Address':'Chennai'},
            32845:{'Name':'Shyam','DOB':date(1985,7,15),
                    'Address':'Chennai'},
            437788:{'Name':'Roopa','DOB':date(1970,2,12),
                    'Address':'Bangalore'}
                    
                    }
#will return only keys
print(customerDB.keys())

#will return only vakues

print(customerDB.values())

print("Key","\t","Value")
for(prop,value) in customerDB.items():
    print(prop,"\n")
    for(k,v) in value.items():
        print(k,"\t",v)
        
print("Searching................") 

searchKey= input('Enter the key')
print(customerDB.get(int(searchKey)))       
        





