from sys import stdin


class Car:
	def __init__(self, nog, color) -> None:
		self.nog = nog
		self.color = color
  
	def printCarInfo(self):
		print("noOfGear: {}".format(self.nog))
		print("color: {}".format(self.color))
		


class RaceCar(Car):
	def __init__(self, nog, color, maxSpeed) -> None:
		super().__init__(nog, color)
		self.maxSpeed = maxSpeed
		
	def printInfo(self):
		super().printCarInfo()
		print("maxSpeed: {}".format(self.maxSpeed))








		
#Driver's code

noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())
		
raceCar = RaceCar(noOfGear,color,maxSpeed)
raceCar.printInfo()
