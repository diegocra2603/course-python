
from pprint import pprint


def deleteBlankSpaces(string):
    return [character for character in string if character != ' ']


def countCharacters(string):
    chars_dict = {}
    for char in string:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def createTuplaOrder(dict):
    return sorted(dict.items(),
                  key=lambda key: key[1], reverse=True)


def getMaxValuesArrayTupla(tuplas):
    max_value = 0
    for item in tuplas:
        if item[1] >= max_value:
            max_value = item[1]

    return [tupla for tupla in tuplas if tupla[1] >= max_value]


def show_finish_message(arrayTupla):
    start_message = f"Los caracteres que mas se repites con {arrayTupla[0][1]} repeticiones son: "
    for tupla in arrayTupla:
        start_message += f" \n - {tupla[0].upper()}"
    return start_message


stringWithoutBlankSpaces = deleteBlankSpaces("aabbccdddeee")
dictionaryWithCountChar = countCharacters(stringWithoutBlankSpaces)
tuplaOrder = createTuplaOrder(dictionaryWithCountChar)
tuplasWhitMaxValues = getMaxValuesArrayTupla(tuplaOrder)

print(show_finish_message(tuplasWhitMaxValues))
pprint(tuplaOrder, width=1)
