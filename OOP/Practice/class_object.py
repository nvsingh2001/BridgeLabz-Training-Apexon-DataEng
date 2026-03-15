class Dog:
    species = "Canis familiaris"

    def bark(self):
        return "Woof!"


dog = Dog()
print(type(Dog))
print(type(Dog.bark))
print(type(dog))


class Animal:
    def speak(self):
        print("Animal Speaking")


def init_cat(self, name, age):
    self.name = name
    self.age = age


Cat = type(
    "Cat",
    (Animal, object),
    {"colour": "white", "__init__": init_cat, "speak": lambda self: print("Meow")},
)
setattr(Cat, "breed", "Persian")
print(getattr(Cat, "breed"))


print(Cat.__dict__)
print(Cat("luna", 2).__dict__)
cat = Cat("Meow", 1)


cat.speak()

print(isinstance(type, object))
print(isinstance(object, type))
print(issubclass(object, type))
print(isinstance(type, object))
