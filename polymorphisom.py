class Point:
    def __init__(self, x, y):   
        self.x=x
        self.y=y
    def sum(self,p):
        return Point(self.x+p.x, self.y+p.y)
    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)
p1=Point(2,3)
p2=Point(4,5)

p3=p1.sum(p2)
print(f"Point 3: ({p3.x}, {p3.y})")

p4=p1 + p2  # This will call the __add__ method this is called operator overloading function
print(f"Point 4: ({p4.x}, {p4.y})")