a = int(input("Enter a 1st Number :"))
b = int(input("Enter a 2nd Number :"))

# before swaping 

print(f"Before swaping 1st Number is {a} and 2nd Number is {b}")

#advance swap

a, b = b, a

# adding swaping

a = a + b
b = a - b
a = a - b

# using ^

a = a ^ b
b = b ^ a
a = a ^ b


# after swaping 
print(f"After swaping 1st Number is {a} and 2nd Number is {b}")
