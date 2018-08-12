#New OOP practice


#@classmethods and @staticmethod


class MyClass:
    def method (self): #regular method. It modifies and reads attributes of the instance
        return 'instance method callled', self

    @classmethod
    def classmethod(cls): #only accesses the class. differene is it can't access attributes of the instance
        return 'class method called', cls

    @staticmethod
    def staticmethod(): #Has no access to the class or object instance
        return 'static method called'

bjj = MyClass()
print(bjj.method()) #is pointing to the instance of the class.the instance has to be there, otherwise this code MycClass.method() would fail. check line 24
print(bjj.classmethod()) #has access to the class itself; doesnt really care about an instance
print(bjj.staticmethod())

MyClass.classmethod() #doesnt fail
MyClass.staticmethod() #doesnt fail
#MyClass.method() #THIS WILL FAIL BECAUSE IT DOESNT HAVE AN INSTANCE


'''WHY WOULD YOU NEED CLASS AND STATIC METHODS'''



class Pizza:

    def __init__(self, radius, ingredients):
       self.ingredients = ingredients
       self.radius = radius
       
    def __repr__(self): #formats as a string
        return f'Pizza({self.ingredients})'

    @classmethod
    def margheritta(cls): #this is making it easier to add more instannces to the class. when the @classmethod is called, it calls the __init__ method and has it initialize the margherita pizza. These methods are good for scaling where you have to add more and more objects to your class.
        return cls(['cheese', 'tomatoes'])


    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod #see, we arent accessing the class or the object. It wont change the state of the object or class. Makes code maintainable
    def _circle_area(r):
        return r ** 2 * math.pi



print(' ')
print(Pizza.margheritta()) #CALLING THE margheritta() class method. the result here is that it actually initillizes the mergheritta pizza object for us- which makes life easier. this code is actually the same  --> print(Pizza(['cheese', 'tomatoes']))
print(' ')
print(Pizza(['cheese', 'tomatoes']))
print(' ')
#If we have a class with a complicated __init__ method, we might want to simplify it by using @classmethods as alternative constructors