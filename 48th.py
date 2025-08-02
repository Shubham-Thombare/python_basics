# Multiple Inheritance

class Animal:

    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is Sleeping")    

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):   
    def hunt(self):
        print(f"This {self.name} is hunting")
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Mishi")

hawk.sleep()
hawk.eat()
fish.sleep()
fish.eat()
rabbit.sleep()
