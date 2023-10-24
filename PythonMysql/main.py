from dbhelper import DbHelper

def main():
    db = DbHelper()
    while True:
        print("********* Welcome *********")
        print()
        print("Press 1 to insert new employee")
        print("Press 2 to display all employee")
        print("Press 3 to delete employee")
        print("Press 4 to update employee")
        print("Press 5 to exit from this program")
        print()

        try:
            choice=int(input())
            match choice:
                case 1:
                    #insert data
                    empid = int(input("Enter Emp id :"))
                    empname = input("Enter Emp name :")
                    empsalary = int(input("Enter Emp salary :"))
                    db.insert_employee(empid,empname,empsalary)
                    pass
                case 2:
                    #display all user
                    db.read_employee()
                    pass
                case 3:
                    #delete employee
                    empid=int(input("Enter Emp id to which you want delete :"))
                    db.delete_employee(empid)
                    pass
                case 4:
                    #update employee
                    empid= int(input("Enter Employee id you want to update :"))
                    db.update_employee(empid)
                    pass
                case 5:
                    break

        except Exception as e:
            print(e)
            print("Invalied Details | try again....")  



if __name__ =="__main__":
    main()