'''
Type - Creational
Name - Factory

Use abstract class to hide object creation logic, Abstraction

'''


from abc import abstractmethod, ABCMeta


class Person(metaclass = ABCMeta):

    @abstractmethod
    def setDetails(self, firstName, lastName):

        self.firstName = firstName
        self.lastName = lastName

    @abstractmethod
    def showDetails(self):
        pass

    # Above defined abstract methods acts as a blueprint for defining the sub classes
    # If these methods are not defined in subclass, This will throw error while instantiating the subclass

class Employee(Person):

    designation = "Employee"

    def setDetails(self, firstName, lastName):
        return super().setDetails(firstName, lastName)
    
    def showDetails(self):

        print(f"Hello from {self.designation} {self.firstName} {self.lastName}" )


class HR(Person):

    designation = "HR"

    def setDetails(self, firstName, lastName):
        return super().setDetails(firstName, lastName)
    
    def showDetails(self):
        print(f"Hello from {self.designation} {self.firstName} {self.lastName}" )


# emp = Employee()
# emp.setDetails("John", "Doe")
# emp.showDetails()

# empHr = HR()
# empHr.setDetails("Jenny", "Doe")
# empHr.showDetails()
        
class createPersonFactory():

    @staticmethod
    def createPerson(firstName, lastName, designation):
        person = eval(designation + "()")
        person.setDetails(firstName, lastName)
        person.showDetails()



            

persons = (
    ('John', 'Doe','Employee'),
    ('Jenny', 'Doe', 'HR')
)

for (firstName, lastName, designation) in persons:

    createPersonFactory.createPerson(firstName, lastName, designation) 
