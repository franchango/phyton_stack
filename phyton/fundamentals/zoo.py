class zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, name,type,age):
        self.animals.append(animal(name,type,age) )
    def add_leon(self, name, age):
        self.animals.append(leon(name,age) )
    def add_tigre(self, name, age):
        self.animals.append(tigre(name,age) )
    def add_oso(self, name, age):
        self.animals.append(oso(name,age) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

class animal:
    def __init__(self, name, type, age):
        self.name=name
        self.type=type
        self.age=age
    def display_info(self):
        print("nombre:", self.name, "age:" ,self.age, "salud:",self.health, "felicidad :",self.happiness,)

class leon(animal):
    def __init__(self,name,age):
        super().__init__(name,"leon",age)
        self.health=30 
        self.happiness=75   

class tigre(animal):
    def __init__(self,name, age):
        super().__init__(name,"tigre",age)
        self.health=25 
        self.happiness=55   

class oso(animal):
    def __init__(self,name, age):
        super().__init__(name,"oso",age)
        self.health=35 
        self.happiness=85 
zoo1 = zoo("Francisco Zoo")
zoo1.add_leon("Simba",20)
zoo1.add_leon("Nala",20)
zoo1.add_tigre("Rajah",10)
zoo1.add_tigre("Shere Khan",10)
zoo1.add_oso("yogi",15)
zoo1.print_all_info()