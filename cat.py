class Cat(): 
    species = "house cat"

    def __init__(self, name, age): 
        self.name = name 
        self.age = age

Penny = Cat("Penny", 9)
Waffle = Cat("Waffle", 3)

print(Penny.name, "is a", Penny.species, "He is", Penny.age, "years old")
print(Waffle.name, "is a", Waffle.species, "He is", Waffle.age, "years old")
