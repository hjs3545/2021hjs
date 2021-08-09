class Circle:
    PI=3.1415
    def __init__(self, name, radius):
        self.name=name
        self.radius=radius
    def area(self):
        return Circle.PI *self.radius ** 2

c1=Circle("C1",4)
print(c1.area())
c2=Circle("C2",4)
c2.PI=1.123213123123
print(c2.area())