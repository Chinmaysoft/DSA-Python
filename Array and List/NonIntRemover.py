Hetero_ele = ["ram",1,True,45.2,8,"Sham",5.2,False]

# print(type(Hetero_ele))
# Creating diffrent datatype lists
bool_lst =[]
int_lst=[]
str_lst=[]
float_lst=[]

for i in Hetero_ele:
    
    if isinstance(i, str):
        str_lst.append(i) # adding Str datatype in string list
        
    elif isinstance(i, float):
        float_lst.append(i) # adding float datatype in float list
        
    elif isinstance(i,bool):
        bool_lst.append(i) # adding boolean datatype in bool list
        
    elif isinstance(i, int):
        int_lst.append(i) # adding int datatype in int list

# Printing a diffrent data type of list

print(f"Real List {Hetero_ele}")

print(f"Boolean List {bool_lst}")
print(f"Int List {int_lst}")
print(f"str List {str_lst}")
print(f"float List {float_lst}")