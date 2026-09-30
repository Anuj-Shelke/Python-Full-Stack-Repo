dict = { "maruti" : 30000, 
        "Tata" : 3000000,
        "Toyota" : 340000,
        "Honda" : 400000,
        "Hyundai": 500000,
        "Mistbushi" : 50000,
        "Chevorlet" : 6000000,
        "Renault" : 400000000,
        "Porshe" : 444444444,
}
print(dict)

for i in dict: 
    print(dict.get(i))

#Functions of a dictionary 
print(len(dict),min(dict),max(dict))
print(sorted(dict))
print(sorted(dict,reverse= True))

#Methods of Dictionary 
dict.update({"BMW":200})
dict.update({"Renault":100})
print(dict)

#Methods to delete 1.Pop 2.Popitem 3.Clear
dict.pop("Porshe")
dict.popitem()
# dict.clear()

print(dict.keys()) #to get only keys 
print(dict.values()) #to get only values 
print(dict.items()) # to get both key and value 

for keys in dict: 
    print(keys)

for c in dict.values(): 
    print(c)

for item in dict.items(): 
    print(item)
total = 0 
for i in dict : 
    total += dict.get(i)
print("total is :",total)

list =[]
for item in dict.values():
    list.append(item); 

print(max(list))


         
