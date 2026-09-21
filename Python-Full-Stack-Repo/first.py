x = "Ram" 

#FUNCTIONS IN STRING 
print(x) # Print the string 
print(x[1]) # to return element present at given index 
print(len(x)) #To give lenght of given string 
print(max(x))  # Give the maximum character according to the ascii value 
print(min(x)) # Give the minimum character according to the ascii value 
print(sorted(x)) #To sort the given string in ascending order 
print(sorted(x,reverse=True)) #To sort the given string in descending order 
#METHODS 
x = "Hello"
print(x.lower()) #TO convert to lower case 
print(x.upper()) # To convert to upper case 
print(x.swapcase()) #To convert upper case to lower case and lower case to upper case 

#CHECKING METHODS 
x = "anuj is a Coder "
print(x.isalnum()) #To check if there are string or number present 
print(x.isdigit()) #To check if there are only spaces present in the given string with spaces not included 
print(x.islower()) #check if all the char are lower 
print(x.isupper()) #check if all the char are upper 
print(x.title())   #Convert the first char of every word in a given string to upper case 
print(x.capitalize()) #Convert only the first char to upper case 
print(x.startswith('an')) #To check if the given word starts with the word 
print(x.startswith(' ')) 
print(x.endswith(' ')) #To Check if the given word ends with the word 
print(x.count('o')) #To count of the number of accurances of given word 
print(x.find('is')) #Checks at what index the given word of char is present 
print(x.find('z')) #Same 

name = input("Enter your name ")
print(type(name),name)

for ch in name: 
    print(ch)
ct = 0 
for ch in name: 
    ct+=1 #To count without using the len function 
print(ct)


