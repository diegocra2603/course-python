def divicion(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    return 5 / n
    
try:
    divicion()
except ZeroDivisionError as e:
    print(e)
