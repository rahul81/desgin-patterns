"""
Type - Creational
Name - Factory

Provides an interfaces for creating families of related of dependent
objects without specifying their concrete classes.

"""

from abc import ABCMeta, abstractmethod

class CarFactory(metaclass=ABCMeta):

    @abstractmethod
    def build_parts(self):
        pass

    @abstractmethod
    def build_car(self):
        pass


class SendanCarFactory(CarFactory):

    def build_parts(self):
        return SedanCarPartsFactory()
    
    def build_car(self):
        return SedanCarAssembleFactory()
    
class SuvCarFactory(CarFactory):

    def build_parts(self):
        return SuvCarPartsFactory()
    
    def build_car(self):
        return SuvCarAssembleFactory()


class CarPartsFactory(metaclass=ABCMeta):

    @abstractmethod
    def build(self):
        pass

class CarAssembleFactory(metaclass=ABCMeta):

    @abstractmethod
    def assemble(self):
        pass

class SedanCarPartsFactory(CarPartsFactory):

    def build(self):
        print("Sedan car parts are built")
    
    def __str__(self) -> str:
        return "<Sedan car parts>"
    

class SedanCarAssembleFactory(CarAssembleFactory):

    def assemble(self, parts):
        print(f"Sedan car is assembled here using {parts}")


class SuvCarPartsFactory(CarPartsFactory):

    def build(self):
        print("Suv car parts are built")
    
    def __str__(self) -> str:
        return "<Suv car parts>"
    

class SuvCarAssembleFactory(CarAssembleFactory):

    def assemble(self, parts):
        print(f"Suv car is assembled here using {parts}")



for carFactory in (SendanCarFactory(), SuvCarFactory()):

    car_parts = carFactory.build_parts()
    car_parts.build()
    car_builder = carFactory.build_car()
    car_builder.assemble(car_parts)

