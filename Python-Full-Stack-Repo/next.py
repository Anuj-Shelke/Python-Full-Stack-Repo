class Product:

    def __init__(self, pid, name, category, price):
        self.__pid = pid
        self.__name = name
        self.__category = category
        self.__price = price

    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid):
        self.__pid = pid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def discount(self, percent):
        discount_amount = self.__price * percent / 100
        self.__price -= discount_amount
        print("Discount applied successfully")
        print("Current Price:", self.__price)

    def increase_price(self, amount):
        self.__price += amount
        print("Price increased successfully")
        print("Current Price:", self.__price)


