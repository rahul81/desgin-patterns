'''
Type - Creational
Name - Factory

Use abstract class to hide object creation logic, Abstraction

'''



from abc import ABCMeta, abstractmethod


class AbstractDegree(metaclass = ABCMeta):

    def info(self):
        pass


class BTECH(AbstractDegree):

    def info(self):
        print("Bachelor of Technology")

    # when object is created it returns this string
    def __str__(self) -> str:
        return "Bachelor of Technology"
    
class MBA(AbstractDegree):

    def info(self):
        print("Master of Bussiness Administration")

    # when object is created it returns this string
    def __str__(self) -> str:
        return "Master of Bussiness Administration"
    
class MTECH(AbstractDegree):

    def info(self):
        print("Master of Technology")

    # when object is created it returns this string
    def __str__(self) -> str:
        return "Master of Technology"



class ProfileAbstractFactory():

    def __init__(self) -> None:
        self._degrees:list = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):   # method must be implemented in sub class
        pass

    def addDegree(self, degree:str):        # not abstract method, optional to implement/override in subclass
        self._degrees.append(degree)

    def getDegrees(self,):
        return self._degrees
    

class ManagerProfile(ProfileAbstractFactory):

    def __init__(self) -> None:
        super().__init__()

    def createProfile(self):
        self.addDegree(BTECH())
        self.addDegree(MBA())


class EngineerProfile(ProfileAbstractFactory):

    def __init__(self) -> None:
        super().__init__()

    def createProfile(self):
        self.addDegree(BTECH())
        self.addDegree(MTECH())


class ProfileCreatorFactory():

    @staticmethod
    def createProfile(name):
        return eval(name+ "Profile()")
    

profiles = ('Engineer', 'Manager')

for profile_name in profiles:
    profile = ProfileCreatorFactory.createProfile(profile_name)
    
    print("Profile - ", profile_name)

    for deg in profile.getDegrees():
        print("Degree -> ", deg)

    print("\n")

