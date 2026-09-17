#Code to Print fabonnaci Series using loop 
i = 0; 
first = 0
second = 1
next = 0
while(i<10):
     print(first)
     next = first+second
     first = second 
     second = next 
    
     i+=1
     

