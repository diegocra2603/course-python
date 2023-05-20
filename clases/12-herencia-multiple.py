class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando Animal")


class Pato(Volador, Nadador, Caminador):
    def programar(self):
        print("programar")


