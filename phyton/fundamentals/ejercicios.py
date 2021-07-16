#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def a():
    for x in range(5, -1, -1):
        print(x)
a()
print("============")
#Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def z(b,c):
    print(b)
    return c
z(1,2)
print("============")
 #crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
 #Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def y (d):
    s=d[0]+ len(d)
    print(s)
y([1,2,3,4,5])
print("============")
#Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False
def y (d):
    
    count=0
    v=[]
    if len(d) == 1 :
        return False
    else:
        for p in range(0, len(d),1):
            if d[p] > d[1] :
                v.insert(count, d[p])
                count+=1
    print(count)
    return v
print(y([5,2,3,2,1,4]))
print(y([5]))
print("============")
#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def h(t,val):
    o=[]
    for x in range(0,t,1):
        o.insert(x, val)
    return o
t = int(input("Tamaño: "))
val = int(input("Valor: "))
print(h(t,val))
