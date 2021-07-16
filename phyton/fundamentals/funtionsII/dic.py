def iterarDiccionarios2(x,lista):
    for i in range (len(lista)):
        print(lista[i][x])

students = [
         {'first_name':  'Michael', 'last_name': 'Jordan'},
         {'first_name': 'John', 'last_name': 'Rosales'},
         {'first_name': 'Mark', 'last_name': 'Guillen'},
         {'first_name': 'KB', 'last_name': 'Tonel'}]

iterarDiccionarios2('first_name',students)