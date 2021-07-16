class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):	# agrega la linea, toma un valor
        new_node = SLNode(val)
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node	# Coloca la lista de la cabecera al nodo que se creó en el paso anterior
        return self	