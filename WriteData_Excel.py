'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
from openpyxl import Workbook

import os
wb = Workbook()
dest_filename = 'TestData_2017.xlsx'
ws2 = wb.create_sheet(title="feb2017")

ws2['A2'] = "Automation Demo"

print(os.getcwd())
wb.save(filename = dest_filename)