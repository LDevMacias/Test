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
class Calculadora(Operaciones):
    def __init__(self, ancho = 50):
        Operaciones.__init__(self)
        self._pantalla = ""
        self.ancho = ancho
        self.pantalla(ancho)

    def __repr__(self):
        return self._pantalla

    def pantalla(self, ancho):
        self.agrega_borde(ancho)
        self.agrega_borde(ancho)
        self.agrega_espacio_borde(ancho)
        self.agrega_espacio_borde(ancho)
        self.agrega_espacio_borde(ancho)
        self.agrega_borde(ancho)
        self.agrega_borde(ancho)

    def agregar_datos(self, datos):
        s = str(datos)
        espacio = len(s)
        self._pantalla = self._pantalla[:(self.ancho * 4)-espacio] + s + self._pantalla[(self.ancho * 4):]
        self.realizar_calculo(datos)
        resultado = str(self.resultado)
        espacio = len(resultado)
        if espacio > self.ancho - 5:
            resultado = "LONG ERROR!"
            espacio = len(resultado)
            self._pantalla = self._pantalla[:(self.ancho * 5) - espacio + 1] + resultado + self._pantalla[                                                                     (self.ancho * 5) + 1:]
        else:
            self._pantalla = self._pantalla[:(self.ancho * 5) - espacio + 1] + resultado + self._pantalla[(self.ancho * 5) + 1:]

    def agrega_borde(self, ancho):
        self._pantalla += "*" * ancho + "\n"

    def agrega_espacio_borde(self, ancho):
        self._pantalla += "*" * 2 + " " * (ancho - 4) + "*" * 2  + "\n"

    def realizar_calculo(self, datos):
        operacion = datos.split()
        if "+" in datos:
            numero_1 = int(operacion[0])
            numero_2 = int(operacion[-1])
            self.suma(numero_1, numero_2)

        elif "-" in datos:
            numero_1 = int(operacion[0])
            numero_2 = int(operacion[-1])
            self.resta(numero_1, numero_2)

        elif "*" in datos:
            numero_1 = int(operacion[0])
            numero_2 = int(operacion[-1])
            self.multiplica(numero_1, numero_2)

        elif "/" in datos:
            numero_1 = int(operacion[0])
            numero_2 = int(operacion[-1])
            self.divide(numero_1, numero_2)

        elif "^" in datos:
            numero_1 = int(operacion[0])
            numero_2 = int(operacion[-1])
            if numero_2 < 1:
                self.radicacion(numero_1, numero_2)
            else:
                self.pontenciacion(numero_1, numero_2)
