'''
Type - Creational
Name - Singleton (Using type)

Very similar to singleton 1 pattern which uses __new__ method of object class.
here __call__ method is used from type class

'''


class SingletonMeta(type):
    __instances = {}  # global class dict to hold the objects

    def __call__(cls, *args, **kwds):

        # return existing instance of class if found in objects dict
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwds)
        
        return cls.__instances[cls]
    
class DBconnector(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.status = 'Not Connected'
    
    def disconnect(self) -> None:
        self.status = "Disconnected"

    def connect(self) -> None:
        self.status = "Connected"


client1 = DBconnector()
print("Client 1 : ", client1)
print("Client 1 status : ",client1.status)

client2 = DBconnector()
print("Client 2 : ", client2) # will use the same object as client 1
client2.connect()

print("Client 2 status : ", client2.status)
print("Client 1 status : ", client1.status)


