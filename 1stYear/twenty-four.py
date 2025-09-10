print("Welcome to Simple Calculator!!")

#getting values from user
no_1 = int(input("What is your first number? "))

#deciding which operation and its steps
print("Now which operation do you wish to use,")
op = int(input("Select 1 for addition, 2 for multiplication, 3 for subtraction, & 4 for division."))
print("1. +")
print("2. *")
print("3. -")
print("4. /")

#getting second number
no = int(input("What is your second number? "))

#using operation and if statement
#addition 
if op == 1:
    print(input(f"What is {no_1} + {no}? "))
    right_ans = no_1 + no

#multiplication
if op == 2:
    print(input(f"What is {no_1} * {no}? "))
    right_ans = no_1*no

#subtraction
if op == 3:
    print(input(f"What is {no_1} - {no}? "))
    right_ans = no_1 - no

#division
if op == 4:
    print(input(f"What is {no_1}/{no}? "))
    right_ans = no_1/no

#our answer
if no == right_ans:
    print("That is correct!")
else:
    print(f"That is incorrect. the correct answer is {right_ans}!")


