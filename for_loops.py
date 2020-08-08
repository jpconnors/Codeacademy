#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:19:39 2020

@author: JP
"""

single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
cubes = [item**3 for item in single_digits]
print(cubes)