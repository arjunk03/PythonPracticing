class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price


class MacBookAir(Product):
    def __init__(self, memory, os):
        Product.__init__(self, "AppleAir", 1529)

        self.__memory = memory
        self.__os = os


class ApplePad(Product):
    def __init__(self, generation):
        Product.__init__(self, "ApplePad", 529)

        self.__generation = generation


class AppleWatch(Product):
    def __init__(self):
        Product.__init__(self, "AppleWatch", 400)


class iPhone(Product):
    def __init__(self, model, storage):
        Product.__init__(self, "iPhone", 999)
        self.__model = model
        self.__storage = storage


class AirPods(Product):
    def __init__(self, version):
        Product.__init__(self, "AirPods", 249)
        self.__version = version


class ProductFactory:
    @staticmethod
    def create(item_name, *args):
        if item_name == "MacBookAir":
            return MacBookAir(*args)
        elif item_name == "ApplePad":
            return ApplePad(*args)
        elif item_name == "AppleWatch":
            return AppleWatch(*args)
        elif item_name == "iPhone":
            return iPhone(*args)
        elif item_name == "AirPods":
            return AirPods(*args)


air = ProductFactory.create("MacBookAir", "16GB", "Sierra")
print(air.__dict__)

# Test new products
iphone = ProductFactory.create("iPhone", "14 Pro", "256GB")
airpods = ProductFactory.create("AirPods", "Pro")
print(iphone.__dict__)
print(airpods.__dict__)
