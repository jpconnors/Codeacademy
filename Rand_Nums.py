#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:50:02 2020

@author: JP
"""

#Random numbers

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
print(random_list)
# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)