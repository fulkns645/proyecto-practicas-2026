numeros = [4, 8, 2, 15, 7]

def numeroMaximo(lista:list[int]):
        
        maximo = lista[0]

        for i in lista:
                if i > maximo:
                        maximo = i
                else:
                        maximo = maximo

        return maximo

print(numeroMaximo(numeros))