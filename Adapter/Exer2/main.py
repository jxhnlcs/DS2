class Quadrado:
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def calcular_area(self) -> int:
        return self.lado ** 2

class QuadradoParaCirculo:
    def __init__(self, quadrado: Quadrado) -> None:
        self.quadrado = quadrado

    def calcular_area(self):
        return 3.14 * (quadrado.lado ** 2)

def calcular_area(forma):
    return forma.calcular_area()

quadrado = Quadrado(2)
circulo = QuadradoParaCirculo(quadrado)
print(calcular_area(quadrado))
print(calcular_area(circulo))