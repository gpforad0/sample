


'''from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):

    def __init__(self,price,size):
        self.price=price
        self.size=size



    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):

    def __init__(self,tag1,price,size):
        super().__init__(price,size)
        self.tag1=tag1


    def scroll(self):
        print("scroll in HpNotebook")

    @abstractmethod
    def click(self):
        print('click in HPnotebook')


class DELL(TouchScreenLaptop):

    def __init__(self, tag2, price, size):
        super().__init__(price, size)
        self.tag2=tag2

    def scroll(self):
        print("scroll in DellNotebook")

    @abstractmethod
    def click(self):
        pass



class HPnotebook(HP):

    def click(self):
        print('click in HPnotebook')


class DELLnotebook(DELL):

    def click(self):
        print('click in Dellnotebook ')




Hpnotebook=HP('3d camera-mainfeature',45000,21)
DellNotebook=DELL('motionsensor',85000,25)


Hpnotebook.scroll()
Hpnotebook.click()
DellNotebook.scroll()
DellNotebook.click()  '''



'''CORRECT SOLUTION '''


from abc import ABC, abstractmethod

class TouchScreenLaptop(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def __init__(self):
        TouchScreenLaptop.__init__(self)

    def scroll(self):
        #super().scroll()
        print("Scroll enabled in HP")

    def click(self):
        pass

class DELL(TouchScreenLaptop):

    def __init__(self):
        TouchScreenLaptop.__init__(self)

    def scroll(self):
        #super().scroll()
        print("Scroll enabled IN DELL")

    def click(self):
        pass

class HPnootebook(HP):
    def __init__(self):
        HP.__init__(self)

    def click(self):
        #super().click()
        print("Click enabled IN HPnotebook")

class DELLnotebook(DELL):

    def __init__(self):
        DELL.__init__(self)

    def click(self):
        #super().click()
        print("Click Enabled in DELLnotebook")

h = HP()
d = DELL()
hn = HPnootebook()
dn = DELLnotebook()

print(h.scroll())
print(d.scroll())
print(hn.click())
print(dn.click())
