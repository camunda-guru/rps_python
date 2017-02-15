'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
import os
import glob

print(os.getcwd())
os.chdir('g:/ebooks')
print(os.getcwd())
pathname='F:\pythonworkspace\AdvancedPython\Fidelity_Day1'
print(os.path.split(pathname))
filename='text.py'
(f,ext)=os.path.splitext(filename)
print(ext)
print(f)

os.chdir('f:/yatrabakup')
filelist = glob.glob('/*.*')
for _ in filelist:
    print(_,"\n")
    
print(os.listdir(path='f:/yatrabakup'))






