# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:31:15 2023

@author: MacKenzie Morgan (mm466818)
"""

#################################
#1.
userVar1 = int(input("Please enter value: "))
userVar2 = int(input("Please enter value: "))
if (userVar1 < userVar2):
    print(str(userVar1) + " is less than " + str(userVar2))
else:
    print(str(userVar1) + " is greater than " + str(userVar2))
    
    
    
    
userVar1 = int(input("Please enter value: "))
userVar2 = int(input("Please enter value: "))
if (userVar1 == userVar2):
    print(str(userVar1) + " is equal to " + str(userVar2))
else:
    print(str(userVar1) + " is NOT equal to " + str(userVar2))
    
    
    
    
    
userVar1 = int(input("Please enter value: "))
userVar2 = int(input("Please enter value: "))
if (userVar1 > userVar2):
    print(str(userVar1) + " is greater than " + str(userVar2))
else:
    print(str(userVar1) + " is less than " + str(userVar2))
    
    
####################################
#2.
saleVol1 = int(input("Please enter a value for sales voume to find out how it is classfied: "))
x = int(20.0)
if (saleVol1 >= x):
    print(format(x, ",.1f") + " is classified as small sales volume ")

########################################
#3.
saleVolData = input("Would you like to view sales volume data: ")
if (saleVolData == "yes"):
    print("Viewing Sales Volume Data")
else: 
    print("Other data is currently not available")
    
    
    
#########################################
#4.
saleVolData = input("Would you like to view sales volume data: ")
saleVol1 = (input("Please enter a value for sales volume: "))
if (saleVolData == "yes"):
    print("Would you like to view sales volume?" + " " + str(saleVolData))
print("Please enter a value for sales volume: " + " " + str(saleVol1))
print(saleVol1 + " is classfied as small sales volume")



saleVolData = input("Would you like to view sales volume data: ")
saleVol1 = input("Please enter a value for sales volume: ")
print("Would you like to view sales volume?" + " " + str(saleVolData))
if (saleVolData == "no"):
    print("Other data is currently not available")



saleVolData = input("Would you like to view sales volume data: ")
saleVol1 = input("Please enter a value for sales volume: ")
if (saleVolData == "yes"):
    print("Would you like to view sales volume?" + " " + str(saleVolData))
print("Please enter a value for sales volume: " + " " + str(saleVol1))
print(saleVol1 + " is classfied as small sales volume")

###########################################################################
#5.
zipCode = [43147, 30303, 30303, 54729, 43147, 30303, 43147, 11354, 49009, 30303, 45701]
city = ["Pickerington" , "Atlanta" , "Atlanta", "Chippewa Falls", "Pickerington", "Atlanta", "Pickerington", "Flushing", "Kalamazoo", "Atlanta", "Athens"]
state = ["OH", "GA", "GA", "WI", "OH", "GA", "OH", "NY", "MI", "GA", "OH"]
income = [65000, 49000, 54000, 114000, 47000, 119000, 60000, 76000, 44000, 47000, 55000]



















