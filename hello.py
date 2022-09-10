print(123)


print('james')

print('jeremy')


class Person:
    def __init__(self,name, profession = None):
        self.name = name
        self.profession = profession

    def greet(self):
        print(f'hello {self.name}')

    def show_job(self):
        print(f'I\'m a cool {self.profession}')

Oliver = Person ('Oliver', 'worker')

Oliver.greet()
Oliver.show_job()
