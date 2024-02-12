class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday! I am now {self.age} years old.")

person1 = Person("Milky", 22)
person2 = Person("Zyra", 19)

person1.say_hello()
person2.say_hello()

person1.have_birthday()
person2.have_birthday()

person1.say_hello()
person2.say_hello()
