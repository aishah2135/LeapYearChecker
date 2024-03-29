# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:42:43 2024

@author: aisha
"""

print("What year would you like to check? ")
year = int(input())

if year % 4 == 0: #is the year cleanly divisible by 4
    if year % 100 == 0: #is the year cleanly divisible by 100
        if year % 400 == 0: #is the year cleanly divisible by 400
            print(f"{year} is a Leap Year!")
        else: 
            print(f"{year} Is Not a Leap Year")  
    else: 
            print(f"{year} is a Leap Year.") #the year is cleanly divisible by 4 but not 100
else: 
            print(f"{year} is Not a Leap Year.")