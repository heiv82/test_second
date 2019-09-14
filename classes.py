class Cat:
    def __init__(self,color,legs, age):
        self.color = color
        self.legs = legs
        self.age = age

felix = Cat("ginger",4, 5)
rover = Cat("brown", 4, 6)
stumpy = Cat("black",4, 8)

print(felix.color, felix.age, felix.legs)

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido","brown")
print(fido.name)
fido.bark()

# Classes can also have class attributes,
# created by assigning variables within the body of the class.
# These can be accessed either from instances of the class, or the class itself.

class Man:
    legs = 2
    def __init__(self,name,age):
        self.name = name
        self.age = age

deiv = Man("Deiv",25)
print(deiv.legs)
print(Man.legs)