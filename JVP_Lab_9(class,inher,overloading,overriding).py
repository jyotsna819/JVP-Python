# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, name, breed="Unknown"):
        super().__init__(name)
        self.breed = breed

    # Method Overriding
    def speak(self):
        print(f"{self.name} barks. Breed: {self.breed}")

    # Method Overloading (simulated using default args)
    def fetch(self, item=None):
        if item:
            print(f"{self.name} fetches the {item}.")
        else:
            print(f"{self.name} fetches a stick.")

# Main
dog1 = Dog("Buddy", "Labrador")
dog1.speak()            # Overridden method
dog1.fetch()            # Overloaded method (no argument)
dog1.fetch("ball")      # Overloaded method (with argument)
