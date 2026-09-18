#Code to print This pattern using both while loop 
# * * * * 
# * * * * 
# * * * * 
# * * * * 
row = 0  
coln = 0 

while(row<4): 
   print("*",end=" ")
   coln = 1 
   while(coln<4):
      print("*",end=" ")
      coln+=1
   print()
   row+=1
