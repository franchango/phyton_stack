#Escribe el código para imprimir una cadena literal que diga "Hola mundo" (# 1)
hw = "Hola %s" % "mundo" 	# con valores literales
print(hw)
# Almacena tu nombre en una variable y luego úsalo para imprimir la cadena "¡Hola {{tu nombre}}!" usando una coma en la función de impresión (# 2a)
first_name = "Francisco"
last_name = "Chango"
print("¡Hola {} {} !".format(first_name, last_name))
# Almacena tu nombre en una variable y luego úsalo para imprimir la cadena "¡Hola {{tu nombre}}!" usando un + en la función de impresión (# 2b)
nombre = "Francisco Chango"
print("¡Hola " + nombre +"!")
#Almacena tu número favorito en una variable, y luego úsalo para imprimir la cadena "¡Hola {{num}}!" usando una coma en la función de impresión (# 3a)
num = 29
print("¡Hola",num, "!")


# 1. TAREA: imprimir "Hola mundo"
print( "Hola mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print( "¡Hola",name, "!" )	# con una coma
print("¡Hola " + name +"!" )	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
nume = "42"
print( "¡Hola",nume, "!" )	# con una coma
print( "¡Hola " + nume +"!" )	# con un + - !Este debería darnos un error! "42" string no numero
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "Me encanta comer {} y {} !".format(fave_food1, fave_food2) ) # con .format()
print(f"Me encanta comer {fave_food1} y  {fave_food2} ") # con una cadena f