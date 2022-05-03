class Person:
	
	def __init__(self):
		self.__name = ""
		self.__age = 0
  
	def setValue(self,name,age):
		self.__name = name
		self.__age = age
	def getValue(self):
		print("The name of the person is {} and the age is {}.".format(self.__name,self.__age))



#Driver code goes here.
p = Person()
name = str(input())
age = int(input())
p.setValue(name,age)
p.getValue()