class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

Perro.patas = 3
mi_perro = Perro("Chancito", 10)
mi_perro2 = Perro("Felipe", 10)
print(Perro.patas)
mi_perro2.patas = 5
print(mi_perro2.patas)
print(Perro.patas)
print(mi_perro.patas)
