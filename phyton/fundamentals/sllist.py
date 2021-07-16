class Snode():
    def __init__(self, valor, next = None, anterior = None):
        self.valor = valor
        self.next = next
        self.anterior = anterior

class Datos():
    def __init__(self):
        self.dato = None

    def agregar_inicio(self, val):
        new_node = Snode(val)
        new_node.next=self.dato
        self.dato=new_node
        if self.dato.next is not None:
            self.dato.next.anterior=self.dato
        return self

    def mostrar_datos(self):
        recorrer = self.dato
        while recorrer != None:
            print('*' * 50, '\n', 'dato\t', self.dato.valor, '\n', '-' * 50)
            print('valor\t', recorrer.valor, '\nnext\t', recorrer.next, '\nanterior\t', recorrer.anterior, '\n',
                  '*' * 50, '\n\n')
            #print('imprimir', recorrer.valor)
            recorrer=recorrer.next
        return self

    def remove_from_back(self):
        recorrer = self.dato
        while recorrer.next != None:
            recorrer = recorrer.next
        recorrer.valor = None
        recorrer.next = None
        recorrer.anterior.next = None
        recorrer.anterior = None
        return self

    def remove_from_front(self):
        recorrer = self.dato
        self.dato=recorrer.next
        self.dato.anterior=None
        return self

    def remove_val(self, val):
        recorrer = self.dato
        while str(recorrer.valor) != val and recorrer.next != None:
            if recorrer.next is not None:
                recorrer=recorrer.next
        if str(recorrer.valor) == str(val) and recorrer.next == None:
            recorrer.anterior.next=recorrer.next
        elif str(recorrer.valor) == str(val) and recorrer.anterior == None:
            self.dato = recorrer.next
            self.dato.anterior = None
        elif str(recorrer.valor) == str(val):
            recorrer.anterior.next=recorrer.next
            recorrer.next.anterior=recorrer.anterior
        else:
            print("Valor ingresado no existe")
        return self

    def insert_at(self, position, value):
        recorrer=self.dato
        for x in range(-1, position-1):
            recorrer=recorrer.next
        new_node = Snode(value)

        #Agregar datos al final
        if  recorrer == None:
            new_node.next = self.dato
            self.dato = new_node
            if self.dato.next is not None:
                self.dato.next.anterior = self.dato
            return self

        #Agrega datos al inicio
        elif recorrer.anterior == None:
            new_node.next = self.dato
            self.dato = new_node
            if self.dato.next is not None:
                self.dato.next.anterior = self.dato
            return self
        #Agrega datos al medio
        elif recorrer.anterior != None and recorrer.next != None:
            new_node.next = recorrer.next
            new_node.anterior = recorrer.anterior
            recorrer.anterior.next=new_node
            recorrer.next.anterior=new_node
        else:
            print("Posición no válida")
        return self

lista=Datos()
lista.agregar_inicio('dato3').agregar_inicio('dato2').agregar_inicio('dato3').agregar_inicio('dato4').agregar_inicio('dato5').insert_at(5,'dato_x').mostrar_datos()
