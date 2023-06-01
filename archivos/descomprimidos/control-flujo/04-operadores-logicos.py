# Los operadores logicos son usados para combinar condiciones y son los siguientes
# and, or, not

gas = False
encedido = True
edad = 18

if not gas and (encedido or edad >= 18):
    print("El carro esta listo para arrancar")
else:
    print("El carro no esta listo para arrancar")
