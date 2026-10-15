n=6
li = []
def factor(n):
    for i in range(1,n//2+1):
        if(n%i==0):
            print(i)
       

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)
    
   

def prime(n):
    for i in range(1,n//2):
        if(n%i == 0 ):
            print("The number is not a prime number ")
        else :
            print("Prime number ")

factor(n)
factorial(n)
prime(n)
# prime reverse base power revrse pallindreom armstrong neon exit factor factorial prime recerse ararmstrong palindrome neon 