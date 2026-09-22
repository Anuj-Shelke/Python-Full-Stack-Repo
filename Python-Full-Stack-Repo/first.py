#Classwork Python Batch 22-09-26
x =[]
print(x,type(x))
x =[10,20,30]
print(x,x[1])

#update 
x[2]=300
print(x)

for i in x: 
    print(i)

#inbuit function 
x =[3,6,7,4]
print(len(x),min(x),max(x),sum(x))
print(sorted(x),sorted(x,reverse=True))

x= [20,30]
x.append(50)
x.insert(0,6000) 
print(x)

x.pop() #Remove the last index element 
print(x)
x.remove(20) #Remove the specific element
print(x)
x.clear() #Clear All 
print(x)

x =[1,2,3,4,6]
x.sort() #Sort the given list asc 
print(x)
y = x.copy() #Copy the given list 
print(y)
x.extend([90,80]) #To append in bulk 
print(x)
print(x.index(3)) # Returns the index of given element 

x.reverse() #Reverse no sorting 
print(x)

x = []
ip = int(input("Enter number of element "))
for i in range(ip):
    ele = int(input("Enter Element : "))
    x.append(ele)
print(x)

x = int(input("Enter number of elementss to insert "))
list = []
for i in range(x): 
    ele = int(input("Enter element "))
    list+= [ele]; 
print(list)


