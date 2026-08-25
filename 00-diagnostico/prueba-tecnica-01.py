edades = [15, 18, 22, 12, 30, 17]

def mayorMenor (lista:list[int]):
    mayores = 0
    menores = 0
    for i in lista:
        if i >= 18:
            mayores += 1
        elif i < 18:
            menores += 1
    return print(f"Mayores de edad: {mayores}\nMenores de edad: {menores}")

mayorMenor(edades)