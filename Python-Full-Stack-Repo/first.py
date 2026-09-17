#Code to check if a number is a perfect Number 
num = 6
i =1 
sum = 0
while(i<=num/2): 
    if(num%i==0): 
        sum = i+sum
    i+=1
if(sum == num):
    print("The number is a Perfect Number ")