from array import *

user_no = int(input("Enter total number you wanted to sort.. \n"))
arr = array('i') # adding only integer values in array

for i in range(user_no): #using for loop to ask user to add numbers in array
    add_val = int(input("Enter Number you want toadd in array :\n"))
    arr.append(add_val) # adding number in array using append function


print(arr)

print("Array in sorted format -> \n ")

print(sorted(arr)) # using sorted function to sort the array value