# lib/dog.py 

from datetime import date


class Dog:
    """
    Dog model for tracking clinic clients.

    Attributes set in __init__:
      - name (str): dog's given name
      - breed (str): breed label
      - age (int): age in years (validated via property; set here via setter)
      - last_checkup (str|None): last checkup date; simple string for now
    """

    def __init__(self, name, breed, age, last_checkup=None):
        # assign through the property for age so validation applies immediately
        self.name = name              # instance attribute
        self.breed = breed            # instance attribute
        self.age = age                # triggers the setter we'll add later
        self.last_checkup = last_checkup  # optional, defaults to None
    
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date

    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")
    
    def get_age(self):
        return self._age
    
    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age")
    
    age = property(get_age, set_age)

fido = Dog("Fido","Golden Retriever", 3, "05/22/2022")
clifford = Dog(
    name = "Clifford",
    age = 2, 
    breed = "Big Red")

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)

balto = Dog("Balto", "Husky", "Not an age")
steele = Dog("Steele", "Husky", -10)