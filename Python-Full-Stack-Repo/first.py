class Employee: 
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 

    @property
    def name(self):
        return self.__name

    @name.setter 
    def name(self, name):
        self.__name = name 

    @property
    def age(self):
        return self.__age  

    @age.setter
    def age(self, age):
        self.__age = age    

e1 = Employee("Anuj", 38)

print("Name:", e1.name)
print("Age:", e1.age)

e1.name = "Shelke"
e1.age = 40

print("Updated Name:", e1.name)
print("Updated Age:", e1.age)
