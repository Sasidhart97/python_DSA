"""
Class: A Blueprint for Objects
A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class will have.   

Attribute
An attribute is a characteristic or property of an object. It's like a variable that belongs to an object.

Method
A method is a function defined within a class. It performs actions on the object's data.

Argument
An argument is a value passed to a function when it is called.

Parameter
A parameter is a variable defined in the function definition to receive the argument.

Constructor
A constructor is a special method that is automatically called when an object of a class is created. It is used to initialize the object's attributes.


Key points:

self refers to the current object instance.
Arguments are passed when you call a function, while parameters are defined in the function definition.
The constructor is essential for initializing object attributes.

"""

class Dog:
    def __init__(self, name, breed):  # Constructor with parameters name and breed
        self.name = name  # Attribute: name
        self.breed = breed  # Attribute: breed

    def bark(self):  # Method
        print(f"{self.name} barks!")

    def fetch(self, item):  # Method with parameter item
        print(f"{self.name} fetches the {item}!")

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")  # Arguments: "Buddy", "Golden Retriever"
dog2 = Dog("Max", "Labrador")

# Accessing attributes
print(dog1.name)  # Output: Buddy
print(dog2.breed)  # Output: Labrador

# Calling methods
dog1.bark()  # Output: Buddy barks!
dog2.fetch("ball")  # Output: Max fetches the ball!