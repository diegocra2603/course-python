operaciones_permitidas_msg = "Las operaciones son suma, multi, div, resta"
mensaje_de_bienvenida = f"""
Bienvenido a la calculadora
Para salir escriba 'salir'
{operaciones_permitidas_msg}
\n
"""

print(mensaje_de_bienvenida)

n1 = int(input("Ingrese un numero: "))


while n1:

    oper = input("Ingrese la operación: ").strip().lower()
    print(operaciones_permitidas_msg)

    while oper != 'salir':

        operaciones_validas = ['suma', 'resta', 'multi', 'div']

        if oper not in operaciones_validas:
            break

        n2 = int(input("Ingrese el siguiente número: "))

        operaciones = {
            'suma': n1 + n2,
            'resta': n1 - n2,
            'multi': n1 * n2,
            'div': n1 / n2
        }

        resultado = int(operaciones[oper])

        n1 = resultado

        print(f"El resultado es {resultado}")

        break

    else:
        break
