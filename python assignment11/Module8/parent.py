class Automobile:
    def __init__(self,__make,__model,__mileage,__price):
        self.__make=__make
        self.__model=__model
        self.__mileage=__mileage
        self.__price=__price
    def set_make(self,__make):
        self.__make=__make
    def set_model(self,__model):
        self.__model=__model
    def set_mileage(self,__mileage):
        self.__mileage=__mileage
    def set_price(self,__price):
        self.__price=__price
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price

       
