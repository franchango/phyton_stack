#1 Básico : imprime todos los enteros del 0 al 150.
for x in range(0, 151, 1):
    print(x)
#2 Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range(5, 1005, 5):
    print(x)
#3 Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for val in range(1, 101, 1):
    if val % 10 == 0:
        print("Coding")
    elif val % 5 == 0:
        print("Coding Dojo")
    else:
        print(val)
    
#4 ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
su = 0
for val in range(1, 501, 1):
    if val % 2 != 0:
        su=su+val
print(su)
#5 Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for x in range(2018, -2, -4):
    print(x)
#6 Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1, 1):
    if x % mult == 0:
        print(x)

#E BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?
cont = 0
for i in range(2, 1000 + 1):
    primos = True
    for j in range(2,11):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
print('\nSon %u números primos' % cont )