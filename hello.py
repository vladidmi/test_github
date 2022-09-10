print(123)


print('james')

print('jeremy')


class Person:
    def __init__(self,name, age=None):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hello {self.name}')

    def show_age(self):
        print(f'My age is {self.age}')

Oliver = Person ('Oliver')

Oliver.greet()

Ham = Person ('Ham',40)

Ham.greet()
Ham.show_age()