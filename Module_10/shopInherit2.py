class ShopWorker:
    _count_workers = 0

    def __init__(self, name1="", age1=0):
        self.name = name1
        self.__age = age1
        self.setting_id()

    def setting_id(self):
        ShopWorker._count_workers += 1
        self.id = ShopWorker._count_workers

    def working(self):
        print("Виконую роботу")

    def __str__(self):
        str_out = "Працівник " + str(self.id) + ": " + self.name + " " + str(self.__age)
        str_out += " всіх працівників " + str(ShopWorker._count_workers)
        return str_out

    @staticmethod
    def info():
        print("В магазині працює: ", ShopWorker._count_workers, " працівників")

    @classmethod
    def naming_shop(cls, name):
        cls.name_shop = name
        return cls.name_shop

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            new_age = -new_age
        self.__age = new_age


class Seller(ShopWorker):
    def __init__(self, name1="", age1=0, cash1=0):
        super().__init__(name1, age1)
        self.cash = cash1

    def __str__(self):
        return super().__str__() + " працює продавцем з готівкою " + str(self.cash)

    def working(self):
        print("Обслуговую покупців")


ShopWorker.info()

worker_one = ShopWorker("Іван", 25)
print(worker_one)
worker_one.working()

print("Назва магазину: ", ShopWorker.naming_shop("Fara"))

seller1 = Seller("Оксана", 28, 3456.50)
print(seller1)
seller1.working()
seller2 = Seller("Марія", 40)
print(seller2)
seller2.working()
print(Seller.name_shop)
print(Seller._count_workers)
