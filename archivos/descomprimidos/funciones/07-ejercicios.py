# def es_palindromo(texto):
#     texto_invertido = texto[ : :-1].lower().replace(' ','').replace(',','').replace('.','')
#     texto_formateado = texto.lower().replace(' ','').replace(',','').replace('.','')
#     return texto_invertido == texto_formateado 

def no_space(texto):
    word = ''
    for n in texto:
        if n != ' ':
            word += n
    return word

def reverse(texto):
    texto_al_reverse = ''
    for n in texto:
        texto_al_reverse = n + texto_al_reverse
    return texto_al_reverse


def es_palindromo(texto):
    texto = no_space(texto).lower()
    texto_al_veres = reverse(texto).lower()
    return texto == texto_al_veres

x = es_palindromo("amo la paloma")

print(x)


# print("Amo la paloma",es_palindromo("Amo la paloma"))
# print("reconocer",es_palindromo("reconocer"))
# print("hola mundo",es_palindromo("hola mundo"))
