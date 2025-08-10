class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(2.5)
]

for shape in shapes:
    print(f"The area is: {shape.area()}")
