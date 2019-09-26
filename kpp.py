class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)
point1.draw()
point1.move()

point2 = Point()
point2.x = 30
print(point2.x)

class Pointed:
     def __init__(self,x,y):
        self.x = x
        self.y = y

pointed1 = Pointed(10,20)
print(pointed1.x)
print(pointed1.y)
pointed1.x = 100
print(pointed1.x)


class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"{self.name} talk")

personObject = Person("Aravind")
personObject.talk()


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def meow(self):
        print("Meow..")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()
cat1.meow()
