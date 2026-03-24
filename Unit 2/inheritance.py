# inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, id):
        self.id = id

class Manager(Person, Employee):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Employee.__init__(self, id)

    def show(self):
        print(self.name, self.age, self.id)


m = Manager("mahi", 18, 1)
m.show()