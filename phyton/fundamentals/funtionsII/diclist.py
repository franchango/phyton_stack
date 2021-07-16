def printInfo(dictado):
    print(dictado.keys())
    clave=[]
    value=[]
    for x in dictado:
        clave.append(x)
        value.append(dictado[x])

    for y in range(len(dictado)):
        print('\n',len(value[y]),clave[y])
        for z in range(len(value[y])):
            print(value[y][z])

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)