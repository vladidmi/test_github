print(123)


print('james')

print('jeremy')


class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f'hello {self.name}')

Oliver = Person ('Oliver')

Oliver.greet()
