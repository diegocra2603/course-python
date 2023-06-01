# El for se utiliza para recorrer una lista de elementos
buscar = 12

for numero in range(5):
    if numero == buscar:
        print("Encontrado", buscar)
        break
    else:
        print("No encontrado", numero)
else:
    print("No se encontró el número", buscar)

for char in "Ultimate Python":
    print(char)
