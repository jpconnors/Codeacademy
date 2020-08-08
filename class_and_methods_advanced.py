#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:46:33 2020

@author: JP
"""

#Python Class and Methods

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  #Create a get_rate method that takes self as a parameter and return .001 multiplied by the price of the vehicle
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  #Create a get_rate method that takes self as a parameter and return .00005 multiplied by the price of the vehicle
  def get_rate(self):
    return self.price_of_insured_item * .00005