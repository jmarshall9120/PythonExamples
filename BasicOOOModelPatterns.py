class Animal:
    def __init__(self, name=None, species=None):
        self.Name = None
        self.species = None
        return

#Inheritance
class Dog(Animal):
    def __init__(self, name):
        self.Name = name
        self.Species = self.__class__
        super().__init__(self.Name, self.Species)
        return
rover = Dog("rover")

#Composition
class Dog(Animal):
    @property
    def Name():
        return self.Animal.Name
    @property
    def Species():
        return self.Animal.Species
    def __init__(self, animal, name):
        self.Animal = animal
        self.Animal.Name = name
        self.Animal.Species = self.__class__
        return
    def __getattr__(self, name):
        return getattr(self.Animal, name, None) or AttributeError
animal = Animal()
rover = Dog(animal, "rover")

#Factory
def Rover():
    kls = copy(__class__)
    return Animal("Rover", kls)

