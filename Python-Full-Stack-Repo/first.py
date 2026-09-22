x = [1,2,3]
count = 0 
even = [] 
odd = []
sum = 0 
min = x[1]
max = 0 
   

for i in x:
    
    
    if(min > i):
        min = i
    if(max < i ): 
        max = i
    count+=1
    sum += i
    if(i%2==0):
        even += [i]
    else: 
        odd += [i] 

    
    

print("minmum element is : ",min) 
print("Maximum element is : ",max)
print("Total Count is : ",count)
print("Total Sum is : ",sum)
print("The odd element is")
print(odd)
print("The even elements is")
print(even)