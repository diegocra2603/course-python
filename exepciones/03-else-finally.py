try:
    n1 = int(input("Ingresa el primer numero: "))
except Exception as e:
    print("Ingrese un valor que corresponda")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempres")