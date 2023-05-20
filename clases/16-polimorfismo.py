
from abc import ABC, abstractclassmethod

class Model(ABC):
    @abstractclassmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("Guardando BBDD")


class Sesion(Model):
    def guardar(self):
        print("Guardar Archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([usuario,sesion])