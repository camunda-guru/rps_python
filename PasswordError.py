'''
Created on 14-Feb-2017

@author: BALASUBRAMANIAM
'''
class PasswordError(Exception):
 
    def __init__(self,status):
        #super(PasswordError, self).__init__(status)
        self.passwordStatus=status
    def exceptionMessage(self):
        return self.passwordStatus