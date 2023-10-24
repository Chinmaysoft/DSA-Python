import mysql.connector as connector


class DbHelper:

    def __init__(self):
        self.con =connector.connect(user='root',
                                    password='admin',
                                    host='localhost',
                                    port='3306',
                                    database="pythontest")
        
        query = "create table if not exists Employee(Empid int primary key,Empname varchar(25) not null, Salary int not null)"
        cur = self.con.cursor()
        cur.execute(query)
        print("Created.. ")

    #insert data into table
    def insert_employee(self,Empid,Empname,Salary):
        query = "insert into employee(Empid,Empname,Salary) values({},'{}',{})".format(Empid,Empname,Salary)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("data is saved..")

    #Show table data    
    def read_employee(self):
        query = "select * from employee"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Emp id :",row[0])
            print("Emp Name :",row[1])
            print("Emp Salary :",row[2])
            print("----")

    #Delete table data 
    def delete_employee(self,Empid):
        query="delete from employee where Empid={}".format(Empid)
        c= self.con.cursor()
        c.execute(query)
        self.con.commit()
        print(f"Employee {Empid} is delete..")

    def update_employee(self,Empid):
        val  = int(input("What you want to update \n 1. Employee name \n 2. Employee Salary \n "))
        match val:
            case 1:
                newName= input("Enter New Employee Name :")
                query="update employee set Empname ='{}' where Empid = {}".format(newName,Empid)
                c = self.con.cursor()
                c.execute(query)
                self.con.commit()
                print("Employee Name is updated")
                self.read_employee()
            case 2:
                newSalary= input("Enter New Employee Salary :")
                query="update employee set Salary ={} where Empid = {}".format(newSalary,Empid)
                c = self.con.cursor()
                c.execute(query)
                self.con.commit()
                print("Employee Salary is updated")
                self.read_employee()        
