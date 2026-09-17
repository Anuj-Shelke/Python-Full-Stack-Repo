#Code to calculate factor 
num = int(input("Enter number to check factors of "))
i = 1
print(f"Factor of Number {num} is :")
while(i<=num/2):
    if(num%i==0):
        print(i)
        i+=1



    

