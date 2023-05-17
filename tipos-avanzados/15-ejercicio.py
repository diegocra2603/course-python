def deleteBlankSpaces(string):
    return [character for character in string if character != ' ']


def countCharacters(string):
    dictonaryChars = {}
    for char in string:
        if char in dictonaryChars:
            dictonaryChars[char] = dictonaryChars[char] + 1
        else:
            dictonaryChars[char] = 1
    return dictonaryChars

def createTuplaOrder(dictionary):
    return [  valor for  valor in dictionary.items() ]

def getMaxValuesArrayTupla(tuplas):

    max_value = 0;
    for item in tuplas:
        if item[1] >= max_value:
            max_value = item[1]
        
    return [ tupla for tupla in tuplas if tupla[1] >= max_value ]


stringWithoutBlankSpaces = deleteBlankSpaces("Hola Mundo")
dictionaryWithCountChar = countCharacters(stringWithoutBlankSpaces)
tuplaOrder = createTuplaOrder(dictionaryWithCountChar)

print(getMaxValuesArrayTupla(tuplaOrder))
