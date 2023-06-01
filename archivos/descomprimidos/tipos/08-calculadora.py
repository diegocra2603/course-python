primer_numero = int(input("Escribe el primer número: "))
segundo_numero = int(input("Escribe el segundo número: "))

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
division = primer_numero / segundo_numero

mensaje = f"""
Para los números {primer_numero} y {segundo_numero},
el resultado de la suma es: {suma},
el resultado de la resta es: {resta},
el resultado de la multiplicación es: {multiplicacion},
el resultado de la división es: {division}
"""
print(mensaje)
