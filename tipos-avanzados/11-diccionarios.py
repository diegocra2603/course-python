punto = {"x": 25, "y": 50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)

if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(valor)


usuarios = [
    {"id":1,"nombre":"Chancito"},
    {"id":2,"nombre":"Feliz"},
    {"id":3,"nombre":"Diego"},
    {"id":4,"nombre":"Juan"},
]

for usuario in usuarios:
    print(usuario["nombre"])
