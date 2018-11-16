class Borg:
    """BORG PATTERN MAKING THE CLASS ATTRIBUTES GLOBAL"""
    _shared_data = {} #Atribute Diccionary
    def __init__(self):
        self.__dict__ = self._shared_data#Make it am attribute dictionary
class Singleton(Borg): # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    # This essentially makes the singleton objects-oriented global varible
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)#Update the attribute dictionary by inserting a new key-value
    def __str__(self):
        return str(self._shared_data)#Returns the attribute dictionary for printing
#Let's create a singleton object and add our first acronym

x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)

z = Singleton(SMTP="Simple Mail Transfer Protocol")
print(z)
