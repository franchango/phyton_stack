#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
d=[-5,2,3,2,-1,-4]
for p in range(0, len(d),1):
    if d[p] > 0 :
        d[p]= "big"
print(d)
print("===========================================")
#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
d=[1,6, -4, -2, -7, -2]
count=0
for p in range(0, len(d),1):
    if d[p] > 0 :
       count+=1
d[p]=count
print(d)
print("===========================================")
#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7
d=[1,2,3,4]
count=0
for p in range(0, len(d),1):
    if d[p] > 0 :
       count+=d[p]
print(count)
print("===========================================")
#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
d=[1,2,3,4]
count=0
for p in range(0, len(d),1):
    count+=d[p]
pro=count/(p+1)
print(pro)
print("===========================================")
#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0
d=[37,2,1, -9]
print(len(d))
print("===========================================")
#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False
d=[37,2,1, -9]
a = len(d)
menor =[]
if a == 0:
       print(False) 
else:
    menor=d[0]
    for p in range(0, len(d),1):
        if d[p] < menor :
            menor=d[p]
    print(menor)
print("===========================================")
#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False
d=[37,2,1, -9]
a = len(d)
mayor =[]
if a == 0:
       print(False) 
else:
    mayor=d[0]
    for p in range(0, len(d),1):
        if d[p] > mayor :
            mayor=d[p]
    print(mayor)
print("===========================================")
#Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
arreglo = [10, 7, 6, 10, 4, 9, 10, 5, 9, 8, 4, 3, 1, 10, 10, 10, 2]
# Para sumar simplemente recorremos el arreglo y aumentamos el valor
suma = 0
for valor in arreglo:
    suma = suma + valor

print(f"La suma es {suma}")
print("El valor máximo es:", max(arreglo))
print("El valor minimo es:", min(arreglo))
# Y el promedio se obtiene dividiendo la suma entre la cantidad de elementos
cantidad_elementos = len(arreglo)
promedio = suma / cantidad_elementos
print(f"El promedio es {promedio}")
#Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
inver=[37,2,1, -9]
print(inver[::-1])