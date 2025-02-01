class Dog:
    species = "Canis lupus familiaris"  

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def display_details(self):
        print(f"Species: {self.species}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print("-----------------------")


dog1 = Dog("Golden Retriever", 3)
dog2 = Dog("Bulldog", 5)

dog1.display_details()
dog2.display_details()
