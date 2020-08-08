class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
#Make a subclass of PotatoSalad with the same inputs     
class SpecialPotatoSalad(PotatoSalad):
#create a new parent constructor for PotatoSalad and make sure it takes the same arguments as potato salad  but this time add raisins to it 
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40