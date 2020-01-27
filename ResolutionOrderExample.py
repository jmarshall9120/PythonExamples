
class MyObject(object):
    Attribute_1 = 'Jay'
    Attribute_2 = 'Becky'

    @property
    def Loosers(self):
        return ["RiffRaff", "LilDicky", "KHIA"]

    @classmethod
    def HardcoreMakeOut(cls, *args):
        return ":{}-{}:".join(p for p in args)
    def __init__(self, clique, *args):
        self.Name = clique
        self.PeopleInClique = list(args)
        
        return
    def NeverHappening(self, *args):
        return ":‑###..".join(p for p in args)
    def __getattr__(self, name):
        if len(self.PeopleInClique) < 5 \
            and not any((p for p in self.Loosers if p in self.PeopleInClique)):
            print("You people need more friends!")
            return self.Loosers
        else:
            return AttributeError


myObj = MyObject("Cool_Kids","Bey","Ariana","Justin","Usher")
myObj.HardcoreMakeOut("Jay", "Becky")

"""
Search Order:
    0. Python passes your attribute name to myObj.__getattribute__(self, name) which 
        begins the resolution order search.
    1. __class__.__dict__ in each class in the __class__.__mro___ for a matching 
        attribute where ___get__ and __set__ are defined (data descriptor).
    2. __dict__ for a matching attribute.
    3. __class__.__dict__ in each class in the __class__.__mro___ for a matching 
        attribute where ___get__ IS defined and __set__ IS NOT (non-data descriptor).
    4. __class__.__dict__ in each class in the __class__.__mro___ for a __getattr__
        method. 
    5. base class "object" has a defined __getattr__ method that is defined like:
        def __getattr__(self, name):
            return AttributeError
"""

x = "Bey"

#Search every class in the __mro__ for a data descriptor (__get__ and __set__).
r = []
for kls in myObj.__class__.__mro__:
    r += [v for a,v in kls.__dict__.items() if a == x and hasattr(a, "__get__") and hasattr(a, "__set__")]

#Search the actual instance.
r += [v for a,v in myObj.__dict__.items() if a == x]

#Search every class in the __mro__ for a non-data descriptor(__get__ only).
for kls in myObj.__class__.__mro__:
    r += [v for a,v in kls.__dict__.items() if a == x and hasattr(a, "__get__")]

#Search every class in the __mro__ for a __getattr__ method.
for kls in myObj.__class__.__mro__:
    r += [v(x) for a,v in kls.__dict__.items() if a == "__getattr__"]

print(r[0])

"""
Our Attributes
    1. Attribute_1 - Class Variable
    2. Attribute_2 - Class Variable
    3. Loosers - Class Data Descriptor Instance
    3. Name - Instance Variable
    4. PeopleInClique - Instance Variable
    5. HardcoreMakeOut - Class Method (Non-Data Descriptor)
    6. NeverHappening - Method (Non-DataDescriptor)
    7. __getattr__ - Magic (class) Method
"""

# __getattribute___
# starts resolution search
myObj.__class__.__mro__ # -> (<class '__main__.MyObject'>, <class 'object'>)
myObj.__class__.__mro__[1].__dict__["__getattribute__"] # -> <slot wrapper '__getattribute__' of 'object' objects>

#Class Data Descriptor Instance
    #notice it has a __set__ even though its defined in the class as read only.
myObj.__class__.__mro__[0].__dict__["Loosers"] # -> <property object at 0x0000017071AF94A8>
myObj.__class__.__mro__[0].__dict__["Loosers"].__get__ # -> <method-wrapper '__get__' of property object at 0x0000017071AF94A8>
myObj.__class__.__mro__[0].__dict__["Loosers"].__set__ # -> <method-wrapper '__set__' of property object at 0x0000017071AF94A8>

#Class Variables
myObj.__class__.__mro__[0].__dict__["Attribute_1"] # -> Jay
myObj.__class__.__mro__[0].__dict__["Attribute_2"] # -> Becky

#Instance Variables
myObj.__dict__["Name"] # -> Cool_Kids
myObj.__dict__["PeopleInClique"] # -> ['Bey', 'Ariana', 'Justin', 'Usher']

#Class Methods
myObj.__class__.__mro__[0].__dict__["HardcoreMakeOut"] # -> <classmethod object at 0x0000017071B0BA90>
myObj.__class__.__mro__[0].__dict__["HardcoreMakeOut"].__get__ # -> <method-wrapper '__get__' of classmethod object at 0x0000017071B19780>
myObj.__class__.__mro__[0].__dict__["HardcoreMakeOut"].__set__ # -> AttributeError: 'classmethod' object has no attribute '__set__'

#Instance Methods
myObj.__class__.__mro__[0].__dict__["NeverHappening"] # -> <function MyObject.NeverHappening at 0x0000017071B140D0>
myObj.__class__.__mro__[0].__dict__["NeverHappening"].__get__ # -> <method-wrapper '__get__' of function object at 0x0000017071B14620>
myObj.__class__.__mro__[0].__dict__["NeverHappening"].__set__ # -> AttributeError: 'classmethod' object has no attribute '__set__'














