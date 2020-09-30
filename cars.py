class car:
  def __init__(self, type = 'N/A', maker = 'N/A', model = 'N/A', color = 'N/A'):
    self.type = type
    self.maker = maker
    self.model = model
    self.color = color

  def write(self):
    f = open("carsList.txt", "a")
    f.write(f"\nModel: {self.model}\nMaker: {self.maker}\nModel: {self.model}\nColor: {self.color}\nType: {self.type}\n")
    f.close()
    return True

def askType():
  choice = input("What Type of Car do you have:\n\ta. Truck\n\tb. Car\n\tc. Van\n\td. Sports Car\n")
  if choice == 'a' or choice == 'A':
    return "Truck"
  elif choice == 'b' or choice == 'B':
    return "Car"
  elif choice == 'c' or choice == 'C':
    return "Van"
  elif choice == 'd' or choice == 'D':
    return "Sports Car"
  else:
    pass

def askMaker():
  maker = input("Who made your car? ")
  return maker

def askModel():
  model = input("What is the model name of your car? ")
  return model

def askColor():
  color = input("What color is your car? ")
  return color

def addCars():
  answer = input("Would you Like to add another car? (Y/N): ")
  if answer == 'Y' or answer == 'y':
    return True
  else:
    return False

cars = [] 
addMoreCar = True
counter = 0
#let the program have add as many cars as we want
while addMoreCar == True:
  print("Please Enter Your car Information: ")
  typeOfCar = askType()
  maker = askMaker()
  model = askModel()
  color = askColor()
  cars.append(car(typeOfCar, maker, model, color))
  addMoreCar = addCars()
  counter += 1
for x in cars:
  x.write()
