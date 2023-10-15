item_price = [] # list and list items
add = 0

user = int(input("How much iteam in list :"))

for i in range(user):
    user_no = int(input("Enter A List Values : "))

    item_price.append(user_no)
    
    add +=user_no # adding list values
    # print(len(item_price))
    
    avg = add/len(item_price) 


print(f"avg value of list is {avg:.2f}") # printing avg value of list