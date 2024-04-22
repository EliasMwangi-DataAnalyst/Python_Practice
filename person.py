class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I am {self.name}. I am {self.age} yearsold and I identify as {self.gender}.")

# Example Usage
person = Person("Elias G", 26, "male")
person.introduce()