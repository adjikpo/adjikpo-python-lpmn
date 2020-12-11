#coding:utf-8

import sys
import os
import time

os.system('clear')

from databaseInit import *

# Wait for 5 seconds
time.sleep(1)
os.system('clear')

#install fake data
print('Add') 
installFixtures()

# addCustomer()
# addBank()
# addAccountBank()

print(81 * "-")
getAllCustomers()
print(81 * "-")
getAllAccountBank()
print(81 * "-")
getAllBanks()
print(81 * "-")
updateCustomer()
print(81 * "-")
print(81 * "-")
print(81 * "-")
print(81 * "-")
print(81 * "-")
