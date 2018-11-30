class Person():
    def __init__(self):
        self.name = None
        self.byear = None
        
    def input(self):
        self.name = input('Прізвище:')
        self.byear = input('Рік народження:')
        
    def __str__(self):
        return '{},{}'.format(self.name, self.byear)

        
class Friend(Person):
    def __init__(self):
        super(Person,self).__init__()
        self.phone = None
        
    def input(self):
        Person.input(self)
        self.phone = input('Номер телефону:')
        
    def __str__(self):
        return 'Прізвище: {}, Рік: {},Телефон: {}'.format(self.name, self.byear, self.phone)
        
        
s=Friend()
s.input()
print(s)
