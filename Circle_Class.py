#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:12:31 2020

@author: JP
"""

#Circle Class


class Circle:
  pi = 3.14
  
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)