from multiprocessing.connection import Client


class Cliente:
    def __init__(self, nombre: str, cantidad: float):
        self.__nombre = nombre
        self.__cantidad = cantidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value: float):
        self.__cantidad = value

    def __str__(self):
        return f"{self.nombre} tiene {self.cantidad}€"

    def depositar(self, num: float):
        self.cantidad = self.cantidad + num

    def extraer(self, num: float):
        self.cantidad = self.cantidad - num

    def mostrarTotal(self):
        print(self.__str__())

class Banco:
    def __init__(self, cliente1: Cliente, cliente2: Cliente, cliente3: Cliente):
        self.__cliente1 = cliente1
        self.__cliente2 = cliente2
        self.__cliente3 = cliente3

    @property
    def cliente1(self):
        return self.__cliente1

    @cliente1.setter
    def cliente1(self, value: Cliente):
        self.__cliente1 = value

    @property
    def cliente2(self):
        return self.__cliente2

    @cliente2.setter
    def cliente2(self, value: Cliente):
        self.__cliente2 = value

    @property
    def cliente3(self):
        return self.__cliente3

    @cliente3.setter
    def cliente3(self, value: Cliente):
        self.__cliente3 = value

    def operar(self):
        return self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad

    def depositoTotal(self):
        print(f"Depósito total: {self.operar()}")

pers1: Cliente = Cliente("Miguelito", 700)
pers1.extraer(100)
pers1.depositar(200)
pers2: Cliente = Cliente("Martita", 500)
pers2.extraer(100)
pers2.depositar(200)
pers3: Cliente = Cliente("Manuelete", 20)
pers3.extraer(100)
pers3.depositar(200)

banco: Banco = Banco(pers1, pers2, pers3)
banco.operar()
banco.depositoTotal()