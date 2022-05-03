class Shape:
    def __init__(self, shapeType) -> None:
        self.__shapeType = shapeType
    def printMyType(self):
        print("{}".format(self.__shapeType))
        
class Square(Shape):
    def __init__(self, shapeType, length) -> None:
        super().__init__(shapeType)
        self.length = length
        
    def calculateArea(self):
        return self.length * self.length        

class Rectangle(Shape):
    def __init__(self, shapeType, length, breadth) -> None:
        super().__init__(shapeType)
        self.length = length
        self.breadth = breadth

    def calculateArea(self):
        return self.length * self.breadth

    
#Your code goes here.
obs = Square(length=5,shapeType="square")
obs.printMyType()
print(obs.calculateArea())
obr = Rectangle(length=5,breadth=4,shapeType="rectangle")
obr.printMyType()
print(obr.calculateArea())
