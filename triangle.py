from forme import Forme

class Triangle(Forme):
    def aire(self):
        return (self.math.sqrt(3) / 4) * self.longueur ** 2

    def perimetre(self):
        return 3 * self.longueur