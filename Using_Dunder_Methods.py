#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:09:49 2020

@author: JP
"""

#Using Dunder Methods

class Atom:
  def __init__(self, label):
    self.label = label
  #Give Atom a __add__(self,other) method that returns a molecule with the two Atoms together in a list  
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine