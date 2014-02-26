import other

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit() # OTHER implicit()
son.override() # CHILD override()
son.altered()  # CHILD, BEFORE OTHER altered()
               # OTHER altered()
               # CHILD, AFTER OTHER altered()
