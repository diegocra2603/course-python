from io import open

# Escritura
# texto = "Hola mundo"

# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# Lectura
# archivo = open("archivos/hola-mundo.txt","r")
# texto = archivo.read()
# archivo.close()
# print(texto)

#  Lectura como lista
# archivo = open("archivos/hola-mundo.txt","r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# With y seek
# with open("archivos/hola-mundo.txt") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)


#Agregar
# archivo = open("archivos/hola-mundo.txt","a+")
# archivo.write("Chau mundo")
# archivo.close()

# lectura y escritura
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito Feliz"
    archivo.writelines(texto)
