class Person:
    pass


person = Person()

setattr(person, "name", "Naman")
setattr(person, "age", 24)
setattr(person, "location", "Mathura")

print(getattr(person, "name"))
print(getattr(person, "age"))
print(getattr(person, "location"))

print(hasattr(person, "name"))

delattr(person, "location")

print(vars(person))
