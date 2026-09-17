#Code to check if a number is a pallidrome of not 
mod = 0
div = 0 
num = 85

while(num > 0 ): 
    div = num%10
    mod = div+mod*10
    num = num//10
print(mod)

if(mod == num):
    print("The number is a Pallindrome ")
else: 
    print("The number is not a Pallindrome")