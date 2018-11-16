#visitor.py
class House(object): #The class being visited
    def accept(self, Visitor):
        '''interface to accept a visitor'''
        Visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)
        

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__



class Visitor(object):
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    '''concrete visitpr electrician'''
    def visit(self, house):
       house.work_on_electricity(self) #note that the visitor now has a reference to the house object

#create an HVAC specialist
hv = HvacSpecialist()

e = Electrician()

home = House()

home.accept(hv)

home.accept(e)
