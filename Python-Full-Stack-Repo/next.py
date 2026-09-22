


x =[90,25,34,56]
ele = 34 
for i in x: 
    if(ele == i): 
        print("Element found")

li = []
for var in range(1,5,2):
    li.append(x[var])
sum = 0 
sqli  = []
for var in li: 
    sqli.append(pow(var,2))
print(sqli)

for var in sqli: 
    if(var % 5== 0): 
        print(var)
        sum+= var 
print(sum)

div = 0 
mod = 0 
sum = 625 
summ = 0   

while(sum>0): 
    mod = sum%10
    print(mod)
    summ = mod ; 
    sum = sum//10
print(summ)
    
     



 


