class Cuenta:
    def __init__(self, titular: str, cantidad: float):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value: str):
        self.__titular = value

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value: float):
        self.__cantidad = value

    def __str__(self):
        return f"{self.titular} tiene {self.cantidad}€"

    def imprimir(self):
        print(self.__str__())

class CajaAhorro(Cuenta):
    def __init__(self, titular: str, cantidad: float):
        super().__init__(titular, cantidad)

    def __str__(self):
        return f"{self.titular} tiene {self.cantidad}€"

    def imprimir(self):
        print(self.__str__())

class PlazoFijo(Cuenta):
    def __init__(self, titular: str, cantidad: float, plazo: int, interes: float):
        super().__init__(titular, cantidad)
        self.__plazo = plazo
        self.__interes = interes

    @property
    def plazo(self):
        return self.__plazo

    @plazo.setter
    def plazo(self, value: int):
        self.__plazo = value

    @property
    def interes(self):
        return self.__interes

    @interes.setter
    def interes(self, value: float):
        self.__interes = value

    def calcImporteInteres(self):
        return (self.cantidad * self.interes / 100)

    def __str__(self):
        return f"{self.titular} tiene {self.cantidad}€, tiene un plazo de {self.plazo}, un interés de {self.interes}, y un total de interés de {self.calcImporteInteres()}"

    def imprimir(self):
        print(self.__str__())

cuenta: Cuenta = Cuenta("Miguelito", 700)
caja: CajaAhorro = CajaAhorro("Martuki", 500)
plazo: PlazoFijo = PlazoFijo("Manuelete", 20, 7, 70)

cuenta.imprimir()
caja.imprimir()
plazo.imprimir()