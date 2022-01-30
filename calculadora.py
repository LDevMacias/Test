class Operaciones:
    def __init__(self):
        self.resultado = 0

    def suma(self, numero_1, numero_2):
        self.resultado = numero_1 + numero_2
        print(self.resultado)

    def resta(self, numero_1, numero_2):
        self.resultado = numero_1 - numero_2
        print(self.resultado)

    def multipica(self, numero_1, numero_2):
        self.resultado = numero_1 * numero_2
        print(self.resultado)

    def divide(self, numero_1, numero_2):
        self.resultado = numero_1 / numero_2
        print(self.resultado)

    def pontenciacion(self, numero, potencia):
        self.resultado = numero ** potencia
        print(self.resultado)

    def radicacion(self, numero, raiz):
        self.resultado = numero ** (1/raiz)
        print(self.resultado)

    def raiz_cuadrada(self, numero):
        self.radicacion(numero, 2)

    def raiz_cubica(self, numero):
        self.radicacion(numero, 3)
