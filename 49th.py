# super()

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
    

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14*self.radius*self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width*self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width*self.height/2}cm^2")
        super().describe()

circle = Circle(color="red", is_filled=True, radius=5) 
square = Square(color="yellow", is_filled=True, width=7)   
triangle = Triangle(color="blue", is_filled=True, width=9, height=10)

#print(triangle.color)
#print(triangle.is_filled)
#print(f"{triangle.width}cm")
#print(f"{triangle.height}cm")
#print("***************")

square.describe()
triangle.describe()
