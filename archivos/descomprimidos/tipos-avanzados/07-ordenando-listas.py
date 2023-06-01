numeros = [2,5,4,3,2,123,43,54]

# numeros.sort(reverse=True) #Ordena la lista seleccionada
numeros2 =sorted(numeros,reverse=True) #Devuleve una nueva lista

print(numeros)
print(numeros2)

usuarios = [
    ["Chancito",4],
    ["Felipe",1],
    ["Pulga", 5]
]

usuarios.sort(key=lambda el:el[1])

print(usuarios)