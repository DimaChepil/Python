class Person():
    def __init__(self):
        self.name = None
        self.sname = None
        self.byear = None
        
    def input(self):
        self.name = input('Name:')
        self.sname = input('Surname:')
        self.byear = input('B.Year:')
        
    def __str__(self):
        return '{},{}'.format(self.name, self.sname, self.byear)

        
class PersonFull(Person):
    def __init__(self):
        super(Person,self).__init__()
        self.phone = None
        
    def input(self):
        Person.input(self)
        self.phone = input('Phone number:')
        
    def __str__(self):
        return 'Name: {}, Surname {}, B.Year: {}, Phone number: {}'.format(self.name, self.sname, self.byear, self.phone)
      
s=PersonFull()
s.input()
print(s)
