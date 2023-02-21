class Class1:
    def __init__(self, name):
        self.name = name
class Class2:
    def __init__(self,age):
        self.age =age

class Class3:
    def hello(self):
        print(f'привет ! я - {self.name}')

class Class4:
    def aged(self):
        print(f'я прожил {self.age} лет')

class Class5(Class4 , Class3,Class2 , Class1):
    def __init__(self,name ,age):
        Class1.__init__(self,name)
        Class2.__init__(self , age)



c = Class5("alim", 101)
c.aged()
c.hello()