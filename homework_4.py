class noppy:
    def __init__(self,name):
        self.name = name

class slaver:
    def __init__(self,age):
        self.age = age

class cunning:
    def noppy():
        pass

class dreamer:
    def slaver():
        pass

class pain(noppy,slaver,cunning,dreamer):
    def __init__(self, name,age):
        noppy.__init__(self,name)
        slaver.__init__(self,age)

    def __str__(self):
        return f'{self.name}, {self.age}'

vrg = pain('Zahro',16)
print(vrg)