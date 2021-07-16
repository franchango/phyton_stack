import random
arr = []
MaximoPorDefecto = 100     # se estable el valor maximo por defecto
MinimoPorDefecto = 0        # valor minimo
def randInt(Minimo = MinimoPorDefecto, Maximo = MaximoPorDefecto):
    if(type(Minimo) == int and type(Maximo) == int and Minimo < Maximo):  # aleatorio entre 50 y 500
        print(f'El Mínimo es {Minimo} y el Máximo es {Maximo}')
        for a in range(Minimo, Maximo, 1):
            arr.append(a)    
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
    if(type(Minimo) != int and type(Maximo) != int):        # número aleatorio entre 50 a 100
        print("Estos no son números, así que serán devueltos los números aleatorios pór defecto.")
        for a in range(MinimoPorDefecto,MaximoPorDefecto,1):
            arr.append(a)    
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
    if(type(Minimo) == int and type(Maximo) != int):        # número aleatorio entre 0 a 50
        print("Solo hay un valor Mínimo")
        for a in range(Minimo,MaximoPorDefecto,1):
            arr.append(a)
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
    if(type(Minimo) != int and type(Maximo) == int):        # número aleatorio entre 0 a 100
        print("Solo hay un valor Mínimo")
        for a in range(MinimoPorDefecto,Maximo,1):
            arr.append(a)
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
randInt(Minimo = 50, Maximo = 500)
randInt(Minimo = '', Maximo = 50)
randInt(Minimo = 50, Maximo = '')
randInt(Minimo = '', Maximo = '')