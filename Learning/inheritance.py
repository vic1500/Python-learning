# Use inheritance by passing the class you want to be inherited as an argument to  the child class that's inheriting
class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    pass #Pass methods allow you to define empty functions and classes without python bugging you about it


class Cat(Mammal):
    def meow(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.walk()
cat.meow()