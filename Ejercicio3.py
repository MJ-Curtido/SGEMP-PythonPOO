class Calculadora:
    def __init__(self, num1: int, num2: int):
        self.__num1 = num1
        self.__num2 = num2

    @property
    def num1(self):
        return self.__num1

    @num1.setter
    def num1(self, value: int):
        self.__num1 = value

    @property
    def num2(self):
        return self.__num2

    @num2.setter
    def num2(self, value: int):
        self.__num2 = value

    def __str__(self):
        return f"Número 1: {self.__num1}, número 2: {self.__num2}"

    def suma(self):
        return self.num1 + self.num2;

    def resta(self):
        return self.num1 - self.num2;

    def multiplicacion(self):
        return self.num1 * self.num2;

    def division(self):
        return self.num1 / self.num2;

    def imprimir(self):
        print(f"Resultados -->\n\tSuma: {self.suma()}\n\tResta: {self.resta()}\n\tMultiplicación: {self.multiplicacion()}\n\tDivisión: {self.division()}")

calc: Calculadora = Calculadora(7, 7)
print(calc.__str__())
calc.imprimir()