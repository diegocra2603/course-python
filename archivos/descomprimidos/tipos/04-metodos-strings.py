animal = "  chanCHito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())  # Cada palabra en mayuscula
print(animal.strip())  # Funciona como el trim de javacript
# Funciona como el trim de javascript solo de lado izquierdo
print(animal.lstrip())
print(animal.rstrip())  # Funciona como el trim de javascript solo de lado derecho
print(animal.find("CH"))  # Devuelve la posicion de la primera ocurrencia
print(animal.replace("nCH", "j"))  # Reemplaza la primera ocurrencia
print("nCH" in animal)  # Devuelve true si encuentra la cadena
print("nCH" not in animal)  # Devuelve true si no encuentra la cadena
