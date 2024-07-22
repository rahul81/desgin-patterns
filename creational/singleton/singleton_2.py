'''
Type - Creational
Name - Singleton (Mono State) Shared State

Multiple objects of same class will shared the state of the class
'''


class Borg():

    _shared = {}

    def __init__(self) -> None:

        self.__dict__  = self._shared


class Singleton(Borg):

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

obj1 = Singleton('object 1')

print("Object 1 val -> ", obj1.name)

obj2 = Singleton('object 2')

print("Object 2 name -> ", obj2.name)
print("Object 1 name -> ", obj1.name)