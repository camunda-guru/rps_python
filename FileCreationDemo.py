'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
import os
import glob
import io
os.chdir('G:\Local Disk\Python')
print(os.getcwd())
if (os.path.exists('G:\Local Disk\Python\SampleData')):
    print("path exists")
else:
    os.mkdir("SampleData")
os.chdir('G:\Local Disk\Python\SampleData')
print(os.getcwd())
pathname=os.getcwd()
filename=input('Enter file name')
filepath=pathname+'\\'+filename
if(os.path.exists(filepath)):
    print("file exists")
    file=open(filename,mode='a')
else:
    print("file not exists")   
    file=open(filename,mode='w')

for dirpath, dirnames, filenames in os.walk("f:/yatrabakup"):
    #print(dirpath)
    os.chdir(dirpath)
    #print('Current Working directory',"-->",os.getcwd())
    fileArray= glob.glob('*.*')
    for fileRef in fileArray :
        if(os.stat(fileRef).st_size > 100000):
            file.write(fileRef)
            file.write("\t")
            file.write("====>")
            file.write("\t")
            file.write(str(os.stat(fileRef).st_size))
            file.write("\n")

file.close()


