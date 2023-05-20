class Ave:
    def __init__(self): 
        self.volador = True

    def vuela(self):
        print("Vuela ave")

class Pato(Ave):

    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        print("vuela pato")

pato = Pato()
pato.vuela()
print(pato.volador)