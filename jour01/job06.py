class Animal:
    def __init__(self, age):
        self.age = age
        
    def vieillir(self):
        self.age += 1
        return "L'age de l'animal est " + str(self.age) + "."

p1 = Animal(0)

result1 = p1.vieillir()

print(result1)
