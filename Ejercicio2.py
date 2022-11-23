class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value: int):
        self.__edad = value

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

    def mayorEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

    def imprimir(self):
        print(self.__str__())

pers1: Persona = Persona("Miguelito", 3)
pers2: Persona = Persona("Martita", 5)
pers3: Persona = Persona("Manuelete", 20)

pers1.imprimir()
pers1.mayorEdad()
print("\n")
pers2.imprimir()
pers2.mayorEdad()
print("\n")
pers3.imprimir()
pers3.mayorEdad()