'''
Created on 14-Feb-2017

@author: BALASUBRAMANIAM
'''
import getpass
print(getpass.getuser())
import hashlib
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())

hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)