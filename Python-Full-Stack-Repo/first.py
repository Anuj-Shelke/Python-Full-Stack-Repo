count = 0 
print("Q1. Count how many words are there in x")
x = "Hi I am python"
y = x.split(" ")
for char in y:
    count+=1 
print(count)

print('Q.2 "Python is easy" Print in Reverse way ')
z = "Python is easy"
w = z.split(" ")
print(sorted( w,reverse = True))


print("Q.3 How r u ----> Find Largerst Word ")
b = "How r u"
a = b.split(" ")
largest_word = max(a, key = len)
print("largest word is : ",largest_word);




print("Q.4 Check string ends with a or not ===> maharashtra ")
v = "maharashtra"
print(v.endswith("a"))




        
        


    
