from parent import Automobile

class car(Automobile):
    
    def __init__(self,__doors,__make,__model,__mileage,__price):
        self.__doors=__doors
        Automobile.__init__(self,__make,__model,__mileage,__price)
    def set_doors(self,__doors):
        self.__doors=__doors
    def get_doors(self):
        return self.__doors

class truck(Automobile):
    
    def __init__(self,__drive_type,__make,__model,__mileage,__price):
        Automobile.__init__(self,__make,__model,__mileage,__price)
        self.__drive_type=__drive_type
    def set_drive_type(self,__drive_type):
        self.__drive_type=__drive_type
    def get_drive_type(self):
        return self.__drive_type

class suv(Automobile):
    
    def __init__(self,__pass_cap,__make,__model,__mileage,__price):
        Automobile.__init__(self,__make,__model,__mileage,__price)
        self.__pass_cap=__pass_cap
    def set_pass_cap(self,__pass_cap):
        self.__pass_cap=__pass_cap
    def get_pass_cap(self):
        return self.__pass_cap

def main():
    c=car('4','abc','efg','45','100')
    t=truck('3','lmn','xyz','76','200')
    s=suv('5','ijk','fgh','80','300')
    c.set_doors(int(input('enter the no. of doors')))
    print(c.get_doors())
    c.set_model(input('enter the model'))
    print(c.get_model())
    t.set_drive_type(input('enter the drive_type'))
    print(t.get_drive_type())
    print(t.get_mileage())
    s.set_pass_cap(input('enter the pass_cap'))
    print(s.get_pass_cap())
main()
