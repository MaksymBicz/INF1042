class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return '...'

    def manger(self):
        return 'yum'

class Chien(Animal):
    def parler(self):
        return 'Wouf !'

class ChienGuide(Chien):
    def parler(self):
        return super().parler() + ' (calme)'

class Chat(Animal):
    def parler(self):
        return super().manger() + ' Meow !'

class Lion(Chat):
    def parler(self):
        return super().parler() + ' (roar)'

fido = Chien("Fido")
print(fido.parler())


lion = Lion("Léo")
print(lion.parler())