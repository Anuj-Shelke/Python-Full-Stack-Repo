# Reverse a Number 
num = int(input("Enter number to reverse "))
num1 = 0
div = 0 
rev = 0 
while(num > 0):
  num1 = num%10
  rev = rev*10+num1
  num = num//10

print("The Reverse of Number is ",rev)