class Circle:
    area=0
    circumference = 0

    def __init__(self,radius=None):
        self.radius=radius

    def setRadius(self,radius):
        self.radius=radius

    def getRadius(self,radius):
        return self.radius

    def getArea(self):
        self.area = (3.14*self.radius*self.radius)
        print("Area of Circle is {}".format(self.area))

    def getCircumference(self):
        self.circumference = (2*3.14*self.radius)
        print("Circumference of circle is %s"%self.circumference)


c1 = Circle()
radius = int(input("Enter a radius of circle to find an arae :"))

c1.setRadius(radius)

c1.getArea()

c1.getCircumference()
