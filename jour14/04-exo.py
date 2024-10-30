class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__ (self, other):
        return Point(self.x + other.x , self.y + other.y)
    
    def __str__(self) :
        # return str(vars(self))
        return f"Point(x={self.x}, y={self.y})"

pt1 = Point(1, 2)
pt2 = Point(3, 4)
pt3 = pt1 + pt2
print(pt3)

