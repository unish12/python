from abc import ABC, abstractmethod
#Abstraction and polymorphism   
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print("Breathing")
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    barks = True

    def make_sound(self):
        print("Barking")

class Human(Animal):
    def make_sound(self):
        print("Speaking")

jimmy:Dog=Dog(name="Jimmy")
jimmy.breathe()
jimmy.make_sound()

unish:Human=Human(name="Unish")
unish.breathe()
unish.make_sound()