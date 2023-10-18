class Person:

    def __init__(self,name,age): # init method using instance objcets values
        self.name=name
        self.age=age

       
    def show(self): # this show  method is show person information
        print(f"Hi {self.name} and your age is {self.age}")


# Getting data from user
name = input("Enter your name : ") 
age = int(input("Enter your age : "))

# p1=Person this is called as call object while creating a class, class object create automatically 

p1=Person(name,age) # At the time of instance object get created it implicitly call __init__() method

p1.show() # the instance object is call show function