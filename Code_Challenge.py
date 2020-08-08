#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:40:11 2020

@author: JP
"""

destinations = ['Paris,France','Shanghai,China','Los Angeles, USA',
                'Sao Paulo,Brazil','Cairo,Egypt']

print(destinations)

test_traveler = ['Erin Wilkes','Shanghai, China',['historical site','art']]


def get_destination_index(destination):
    destination_index=destinations.index(destination)
    return destination_index

print(get_destination_index("Los Angeles, USA"))