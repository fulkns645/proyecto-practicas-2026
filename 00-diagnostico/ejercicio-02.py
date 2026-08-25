num = int(input("Hola, en este modulo se realiza un ciclo y para hasta el numero entero positivo que pongas \nPD: No pongas un numero muy largo: "))

if num == 0:
    print("Es 0")
elif num < 0:
    print("Es Negativo")
else :
    for i in range(1, num+1) :
        
        print(i)


