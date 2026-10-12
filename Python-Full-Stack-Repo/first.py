class Product: 
    def __init__(self, id,name,price,qty):
        self.__id = id 
        self.__name = name
        self.__price = price 
        self.__qty = qty
        
    @property
    def name(self):
        return self.__name

    @name.setter 
    def name(self, name):
        self.__name = name 

    @property
    def  id(self):
        return self.__id  

    @id.setter
    def id(self, id):
        self.__id= id    

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        self.__price = price

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self,qty):
        self.__qty = qty

p1 = Product(1,"Bottle",20,1)

print("Id",p1.id)
print("Name:", p1.name)
print("Price:", p1.price)
print("Qty",p1.qty)

