class Team:
    team_lst = [] # class valiable list

    def __init__(self,member_lst= None): # init method
        self.member_lst = member_lst

    def MemberNames(self,member_lst): # main method to get values from user
        members_no= int(input("How many members in your team :"))

        for i in range(members_no):
            user_name  =input("Enter your team member name : ")
            member_lst.append(user_name)
        self.team_lst = member_lst

    def DisplayNames(self): # display the list of team memebers 
        print("Your team members are ... \n ",self.team_lst)
                


#Empty list
member_lst =[]

t1 = Team() #Instance of class object

t1.MemberNames(member_lst) # function of class given as empty list

t1.DisplayNames() # display function of class