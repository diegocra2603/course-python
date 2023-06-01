class Model():
    tabla = False
    def __ini__(self):
        if not self.tabla:
            print("Tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()

usuario.guardar()
usuario.buscar_por_id(123)