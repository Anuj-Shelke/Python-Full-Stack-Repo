#Code to check if a number is a Strong number 
#Number is a strong number if sum of its factor is number itself eg 145 
num = 145
temp = num
fact = 1
sum =0 
while(num >0):
    mod  = num%10
    fact = 1
    for i in range(mod,0,-1): 
      fact = fact*i
      
    sum = sum+fact
    num = num//10


if(sum == temp):
   print("The number is a strong number ")
else : 
   print("not a strong num")
  

