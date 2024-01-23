lista = [12, 33, 54, 221, 453, 43, 22, 43, 12, 221, 12]
diccionario = {}
for num in lista:
    if num in diccionario:
        diccionario[num] +=1
    else:
        diccionario[num] = 1
print(diccionario)