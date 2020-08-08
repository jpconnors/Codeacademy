#Class_And_Methods

class SortedList(list):
#Create an append method that takes two arguments, self and value
  def append(self, value):
#Write the code that would get SortedList to behave like a normal list when calling the .append() method.   
  super().append(value)
    self.sort()