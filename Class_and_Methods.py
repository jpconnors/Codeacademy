#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:43 2020

@author: JP
"""

#Class and Methods


class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self,miles):
        return miles*self.kms_in_a_mile
    
    
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)    
print(kms_in_5_miles)