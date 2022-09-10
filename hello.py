print('james 1')

print('jeremy')


class Person:

    def __init__(self,name, age=None, profession = None):
        self.name = name
        self.age = age
        self.profession = profession


    def greet(self):
        print(f'hello {self.name}')


    def show_age(self):
        print(f'My age is {self.age}')
    
    def show_job(self):
        print(f'I\'m a cool {self.profession}')

Oliver = Person ('Oliver')

Oliver.greet()

Ham = Person ('Ham',40)

Ham.greet()
Ham.show_age()



Oliver = Person ('Oliver', '','worker')

Oliver.greet()
Oliver.show_job()
