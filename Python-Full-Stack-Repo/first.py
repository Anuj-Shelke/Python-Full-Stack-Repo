list1 = [[10,20,30],
         [40,50,60],
         [70,80,90]]
element = 100
flag = True
for i in list1:
    for j in i:
        if element == j:
            print("element found ")
            flag = False
if flag == True:
    print("Element not found ")      

 
     



 


