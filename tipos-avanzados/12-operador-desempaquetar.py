# lista1 = [1, 2, 3, 4]

# # print(1, 2, 3, 4)
# # print(*lista1)

# lista2 = [5, 6]

# combinada = ["Hola", *lista1, "Mundo", *lista2, "Chancito"]
# print(combinada)

punto1 = {"x": 19, "y": "Hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1,"lala":"Hola Mundo", **punto2, "z": "mundo"}

print(nuevoPunto)
