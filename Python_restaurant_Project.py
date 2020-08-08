#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:26:31 2020

@author: JP
"""

#Python Class Project
class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
#Lets create a franchise class
class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return self.address
#remember, self refers to the object that gets returned from the constructor 

#Now tell customers what they can order
  def available_menus(self,time):
    available_menus = []
    for menu in self.menus:
      if time >=menu.start_time and time <=menu.end_time:
        available_menus.append(menu)
    
    
    return available_menus

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
 
#Give menu a calculate bill method that has two parameters
  def calculate_bill(self,purchased_items):
    #define a starting variable
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
  
#3Create your Brunch Menu  
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

#Create a menu array that contains all of the menus

menus = [brunch_menu,early_bird_menu,dinner_menu,kids_menu]

flagship_store = Franchise('1232 West End Road',menus)

new_installment = Franchise('12 East Mulberry Street',menus)



print(kids_menu)
#Test calculate_bill()
print(brunch_menu.calculate_bill(['pancakes','home fries','coffee']))

print(flagship_store)


#test available menus

print(flagship_store.available_menus(2000))


basta = Business("Basta Fazoolin with my heart",[flagship_store,new_installment])

#Arepa

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a' Arepa",arepas_items,1000,2000)

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

arepa = Business("Take a' Arepa",[arepas_place])

print(arepa.franchises[0].menus[0])

#Now we are starting to get into object oriented programming. This enables us to create classes with class hierarchies to represent real life objects