#Code to Check if a number is a perfect Number 
i =1
sum = 0
num = int(input("Enter number to check"))
while(i <=num/2):
    if(num%i==0):
        sum = i+sum
    i+=1
print(sum)
if(sum == num):
    print("The number is a perfect Number ")
else: 
    print("The number is not a perfect Number ")

    

