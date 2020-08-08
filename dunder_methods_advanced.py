#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:15:07 2020

@author: JP
"""

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  #Give LawFirm a __len__ method that will return the number of lawyers in the law firm  
  def __len__(self):
    return len(self.lawyers)
  #Give LawFirm a __contains__ method that will check two parameters: self and lawyer and checks to see if lawyer si in self.lawyers 
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])