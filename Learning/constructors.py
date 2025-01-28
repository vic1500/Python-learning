# A constructor is a function that gets called at the time of creation of an object
class Point:
    # to define a constructor we do;
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

point1 = Point(1, 2)
point1.x = 11
print(point1.x, point1.y)

# Exercise

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"Hi, I am {self.name} and I am {self.age}")
    def talk(self, message):
        print(f"{message}")
    def move(self):
        print("I am moving now even though I am {} years old".format(str(self.age)))

john = Person("John", 36)

john.intro()
john.talk("I work as an entrepreneur")
john.move()