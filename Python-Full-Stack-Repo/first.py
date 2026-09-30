#Methods of Tupple 
tup = (1,2,3,4,5)
print(tup.count(5)) #Count the occurance of given input element 
print(tup.index(3)) #Returns the index of the input element 
li = [1,2,3,4]
tup1 = (li,23,4,5,6) #We can make a tupple mutable by adding a list to it 
li.append(5)
print(tup1)

#Printing tup using for loop 
for i in tup1: 
    print(i)
student =[]
j = 0 ; 
for i in range(1,4):
    i = input("Enter marks"); 
    student.insert(j,i)
    print(list)
    j+=1 
student = (
    ("amit",70,80,90),
    ("Ajay",67,77,99),
    ("Mahesh",100,100,99)
)

student = []
i = int(input("Enter number of users ")); 
k  = 1

p = 1 
for j in range(0,i):
    
    name = input("Enter name of user "); 
    student.append(name)
    k+=1
    print("Enter marks of  3 subjects "); 
    m1 = int(input("English : "))
    student.append(m1)
    m2 = int(input("Maths : "))
    student.append(m2)
    m3 = int(input("Marathi : "))
    student.append(m3)
   

    for i in student: 
        total = m1+m2+m3
    
print("total of ",i,"is ",total)

print(student)
    

