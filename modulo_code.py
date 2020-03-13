#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:30:42 2020

@author: JP
"""

#Modulo_code


# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False