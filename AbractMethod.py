'''Creating abstract class:
by importing abc module we can create abstract class from any class, abstract class have a one abstract method without any
factionality(here Offer method ),that method should always be in its child classes otherwise it will give error and other things is that when class
 become abstract class u can not create object for that class
 here parent class samsung will become abstract class

 MYchoi: abstact method is used when all child classes of a parent class need one common method but different functionality so
 we need to give PASS to abstract function of parent class.  here all Samsung phone has offer but offer is different for all phone
 so here we have abstract method is Offer but each child class has different functionality inside Offer method

 In general term we can say that by using @abstractmethod we make that function interface between parent and all child class

 when all method in class become abstraxt method then that class becomes abstract class which does not have any implementation
 bcoz implementation is done by all of its child class.

 '''

from abc import abstractmethod,ABC
class samsung(ABC):
    def __init__(self,country,year,size):
        self.country = country
        self.year = year
        self.size = size

    def silentmode(self):
        print("phone in silent mode")

    @abstractmethod
    def Offer(self):
        pass
        # print("fg")   mychoi:  Technically , functionality in this method is of no use,bcoz it of its child class has this method



class Galaxy(samsung):
    def __init__(self, price, country, year, size):
        samsung.__init__(self, country, year, size)  # inspite of this : super().__init__(country, year, size)
        self.price = price

    def Galaxyfeature(self):
        print("galaxy has the motion sensor")
        #super().silentmode()  to access method of parent class we can use super()

    def Offer(self):
        print("Yes, There is a offer now in this phone")


class Note(samsung):
    def __init__(self, series, country, year, size):
        samsung.__init__(self,country, year, size)
        self.series = series

    def Notefeature(self):
        print("note has the 3d-camera ")

    def Offer(self):
        print("Yes, There is a offer now in this phone")


J7=Galaxy(7000,'india',2018,'normal')
Note10=Note(10,'canada',2019,'Large')


print(J7.price)
print(J7.country)
print(J7.year)
print(J7.size)
J7.silentmode()
J7.Galaxyfeature()
J7.Offer()

print("")
print('')
print(Note10.series)
print(Note10.country)
print(Note10.year)
print(Note10.size)
Note10.silentmode()
Note10.Notefeature()
Note10.Offer()

##   's=samsung()'  u cann't do it bcoz abstract class can not have any object, it will give error
