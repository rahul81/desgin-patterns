'''
Type - Creational
Name - Singleton

When only 1 instance/object of class should be created to be used every time, 
same object will be used every time
No new objects will be created.
'''


class SingleTon(object):

    def __new__(cls, *args, **kwargs):

        # if object of class does not exists then create and object 
        # else return existing object 
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)

        return cls._instance

obj1 = SingleTon()
obj1.name = 'object 1'

print(f"Object 1 name -> {obj1.name}" )

obj2 = SingleTon()
print(f"Object 2 name -> {obj2.name}")


