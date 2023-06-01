# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2


# comando = ""

# while comando.strip().lower() != "salir":
#     comando = input("Escribe un comando: ")
#     print(comando)

while True:
    comando = input("Escribe un comando: ")
    if comando.strip().lower() == "exit":
        print("Saliendo...")
        break
