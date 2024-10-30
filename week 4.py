# Creating the class
class Person:
    # Constructor to initialize the attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to display the information
    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and my gender is {self.gender}."

# Creating an instance of the Person class
person = Person("Mary", 32, "Female")

# Calling the introduce method to display the person's information
print(person.introduce())

 


