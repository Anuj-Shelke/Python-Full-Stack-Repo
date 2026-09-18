#Code to print Right Angle Triangle 
n = 4 
i = 1 
while i < n+1: 
    k = 1
    while k< n-1: 
        print(" ",end="")
        k+=1
    j=1
    while(j<=i): 
        print("*",end="")
        j+=1
    print()
    i+=1 
#Same using for loop 


for i in range(1,n+1):
    print(" "*(n-i)+("*"*i))



    


