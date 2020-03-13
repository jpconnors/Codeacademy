weight=10000

def ground_ship_cost(weight):
  if weight <=2:
    ground_price=1.50*weight+20
  elif weight >2 and weight<=6:
    ground_price=3.00*weight+20
  elif weight >6 and weight<=10:
    ground_price = 4.00*weight+20
  else: ground_price = 4.75*weight+20
  return ground_price

def drone_ship_cost(weight):
  if weight <=2:
    drone_price=4.50*weight
  elif weight >2 and weight<=6:
    drone_price=9.00*weight
  elif weight >6 and weight<=10:
    drone_price = 12.00*weight
  else: drone_price = 14.25*weight
  return drone_price  

def optimal_shipping(weight):
  if ground_ship_cost(weight) <drone_ship_cost(weight) and drone_ship_cost(weight)< 125:
      return ground_ship_cost(weight), "ground shipping is cheapest"
  if drone_ship_cost(weight)<ground_ship_cost(weight) and drone_ship_cost(weight)< 125:
      return drone_ship_cost(weight), "drone shipping is cheapest"
  else: return 125,"premium ground shipping is cheapest"

print(optimal_shipping(weight))