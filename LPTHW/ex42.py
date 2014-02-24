## Animal is-an object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-an Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-an object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Person is-an Employee
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## satan is mary's pet
mary.pet = satan

## frank is-an employee with a 12000 salary
frank = Employee("Frank", 12000)

## rover is frank's pet
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
