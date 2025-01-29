# When defining classes, we capitalize each new words rather than using _ to separate them like functions and variables. It's called the skoll naming convention
class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

point1 = Point()
point1.x = 100
point1.y = 200
print(point1.x, point1.y)

point1.draw()

point2 = Point()
point2.x = 300
point2.y = 400
print(point2.x, point2.y)