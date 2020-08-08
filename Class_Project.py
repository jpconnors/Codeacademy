#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:26:31 2020

@author: JP
"""

#Python Class Project

#1) Create a menu class for the restaurant 

class Menu:
  #2) Give menu a constructor with six parameters
  def __init__(self, name, items, start_time, end_time):
      self.name=name
      self.items=items
      self.start_time=start_time
      self.end_time=end_time
  
  
   #Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self):
      return self.name +' menu available from '+str(self.start_time) + ' - ' +str(self.end_time)
 
  
  
  
  
#Create your Brunch Menu  
brunch_items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu=Menu('Brunch',brunch_items,1100,1600)

print(brunch_menu.name)


#Create your Early Bird Menu  
early_bird_items={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu=Menu('Early Bird',
                     early_bird_items,1500,1800)

dinner_items={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu=Menu('Dinner',
                     dinner_items,1700,2300)

kids_items={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu=Menu('Kids',
                     kids_items,1100,2100)


print(brunch_menu)



