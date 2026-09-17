#Code to Reverse a Number 
num = 21
div = 0
mod = 0

while(num> 0):
    div = num%10     
    mod = div+mod*10
    num = num//10
   
print(mod)    
    
