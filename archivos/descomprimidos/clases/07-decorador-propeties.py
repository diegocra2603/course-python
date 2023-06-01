class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print("Pasando por geeter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por seeter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
