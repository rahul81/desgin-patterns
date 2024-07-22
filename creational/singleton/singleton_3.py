'''
Type - Creational
Name - Singleton (Using decorator class)

Multiple objects of same class will shared the state of the class
'''

class SingletonDecorator():

    def __init__(self, klass) -> None:
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):

        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)

        return self.instance
    
@SingletonDecorator
class Logger():

    def __init__(self):
        self.start = None

    def write(self, message:str):

        if self.start:
            print(self.start, message)
        else:
            print(message)

    
logger1 = Logger()
logger1.start = '$ '

print("logger1 object -> ", logger1)
logger1.write("Logger1 object is created")

logger2 = Logger()
print("logger2 object -> ", logger2) # will point to same object created earlier
# will use the same start prefix as logger1
logger2.write("Logger2 object is created")