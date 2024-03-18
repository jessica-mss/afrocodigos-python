class Animal:
    nome = "nome do meu animal"
    def __init__(self, patas):
        self.numero_patas = patas
        
class Mamifero:
    nome = "nome do meu mamifero"
        
class Gato(Animal, Mamifero):
    def som(self):
        return "Miau"

class Cachorro(Animal):
    def som(self):
        return "Au au"
