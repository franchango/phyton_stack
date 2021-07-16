class Tienda:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.lista_productos = []

 
    
    def add_product(self, new_product):
        self.lista_productos.append(new_product)
        return self
    
    def sell_product(self, id):
        self.lista_productos.pop(id)
        return self
    
    def inflation(self, percent_increase):
        for product in self.lista_productos:
            product.update_price(percent_increase,True)
        return self
    
    def sell_product_id(self,id):
        self.lista_productos = list(filter(lambda x:x.id != id,self.lista_productos))
        return self
    
    def set_clearance(self, category, percent_discount):
        for product in self.lista_productos:
            if product.categoria == category:
                product.update_price(percent_discount,False)
        return self
    
    def print_tienda(self):
        print(f"\nTienda: {self.nombre}")
        for producto in self.lista_productos:
            producto.print_info()
    