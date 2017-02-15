'''
Created on 13-Feb-2017

@author: BALASUBRAMANIAM
'''
'''
data=[4389,67.78,'training',True]
for elem in data:
    print(elem,"\n")
'''
list1=[]
list2=[]
import random
for i in range(10):
    list1.append(random.randint(1,100))
    list2.append(random.randint(1,100))
print("List  1 sorting...")    
list1.sort(key=None,reverse=True)
print(list1)
print("list2")
list2.sort(key=None)
print(list2)

list3=[list1,list2]
print(list3)

names=['HCL','TCS','Fidelity','IBM']
names.sort(key=None)
print(names)

print(names[1:4:2])
#for charData in range('a'...'z')
print(list(range(2,10)))

list1=[5,6,8,9,10,12]
list2=[56,78,89,91]
#61,84,97,100
list3=[]
for(x,y) in zip(list1,list2):
    list3.append(x+y)
    
print(list3)
len1=len(list1)
len2=len(list2)
print(len1)

if(len1 > len2):
    print(list1[len2:])
    
#tuples
tupleData=(3579,'35769',True)
print(tupleData)
#tupleData.append(5679)
nestedTuple=(list1,list2)
print(nestedTuple)

for _ in nestedTuple:
    for data in _:
        print(data)

data = tuple(range(1,20))

print(data)

result = tuple((map(lambda x:bin(x),data)))
print(result)



















