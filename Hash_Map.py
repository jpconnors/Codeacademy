#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:24:10 2020

@author: JP
"""


#1) Create a class called HashMap.
"""
2) Give HashMap a constructor which takes both 
self and array_size as parameters. array_size 
should be assigned to an instance variable of 
the same name (.array_size), and represents
 the size of the array.

"""

"""3) Create an instance variable called .array,
 which is a list of size array_size. Make each 
 element of .array equal to None.


"""

class HashMap:
  def __init__(self,array_size):
    self.array_size=array_size
    self.array = [None for i in range(self.array_size)]