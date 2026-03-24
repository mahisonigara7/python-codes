# polymorphism

class Vehicle:
    def move(self):
        print("moving")

class Car(Vehicle):
    def move(self):
        print("driving")

class Cycle(Vehicle):
    def move(self):
        print("pedaling")

c1 = Car()
c2 = Cycle()

c1.move()
c2.move()