class Person:

    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

       
    def show():
        print(f"Hi {self.name} and your age is {self.age}")



name = input("Enter your name : ") 
age = int(input("Enter your age : "))

p1=Person(name,age)

p1.show()