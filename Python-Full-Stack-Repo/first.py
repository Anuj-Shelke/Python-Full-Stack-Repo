#Code to check if a number is a neon number 
#A number is a neon number when sum of its digits square is equal to the number itself 

num = int(input("Enter number to check "))
square = num**2
sum = 0
while(square > 0):
    sum = square%10+sum
    square = square//10
if(num == sum):
    print("The number is a neon number ")
else: 
    print("The number is not a neon number ")


