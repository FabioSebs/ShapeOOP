import math

class Shape():
    
    def __init__(self, color="red", filled=True):
        self._color = color
        self._filled = filled
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color:str):
        self._color = color
        
    @property
    def filled(self):
        return self._filled
    
    @filled.setter
    def filled(self , filled:bool):
        self._filled = filled
        
    def __str__(self):
        return f'This is the shape class - Color = {self.color}  Filled = {self.filled}'
    

class Circle(Shape):
    
    def __init__(self, color = "red", filled=True, radius = 1.0):
        
        super().__init__(color, filled)
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius:float):
        self._radius = radius
        
    @property
    def area(self):
        return(math.pi * (self.radius**2))
    
    @property
    def perimeter(self):
        return(2*math.pi*self.radius)
        
    def __str__(self):
        return super().__str__() + f' , This is the Circle class that extends from Shape Class, radius = {self.radius} , area = {self.area} , perimeter = {self.perimeter}'
        
class Rectangle(Shape):
    
    def __init__(self, color="red", filled = True, width = 1.0 , length = 1.0):
        super().__init__(color , filled)
        self._width = width
        self._length = length
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width:float):
        self._width = width
        
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length:float):
        self._length = length
        
    @property
    def area(self):
        return self.length*self.width
    
    @property
    def perimeter(self):
        return(self.length+self.width)*2
    
    def __str__(self):
        return super().__str__() + f', This is the Rectangle class that extends from Shape Class , width = {self.width} , length = {self.length} , area = {self.area} , perimeter = {self.perimeter}'
        
class Square(Rectangle):
    
    def __init__( self, side:float, filled = True, color="red" , width = 1.0 , length = 1.0):
        super().__init__(color, filled, width, length)
        self._side = side
        self.setWidth()
        self.setLength()
        
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, side:float):
        self._side = side
        self.setWidth()
        self.setLength()
    
    def setWidth(self):
        Rectangle.width =self.side
    
    def setLength(self):
        Rectangle.length = self.side
    
    def __str__(self):
        return super().__str__() + f', This is the Square Class that extends from the Rectangle Class, sides = {self.side}, {self.side}, {self.side}, {self.side}'
        
        
        
if __name__ == "__main__":
    #Shape Test
    shape = Shape("green" , True)
    print(shape.__str__())
    shape.color = "yellow"
    shape.filled = False
    print(shape.__str__())
    
    #Circle Test
    circle = Circle("blue" , True , 10.0 )
    print(circle.__str__())
    circle.radius = 20.0
    print(circle.__str__())

    #Rectangle Test
    rectangle = Rectangle("purple" , False , 20.0 , 30.0)
    print(rectangle.__str__())
    rectangle.length = 10.0
    rectangle.width = 10.0
    print(rectangle.__str__())
    
    #Square Test
    square = Square(4.0 , True , "brown" )
    print(square.__str__())
    square.side = 5.0
    print(square.__str__())