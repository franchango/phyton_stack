class Producto:
    def __init__(self,nombre, precio, categoria,id=0) -> None:
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.precio += self.precio * (percent_change/100)
        else:
            self.precio -= self.precio * (percent_change/100)
        return self
    
    def print_info(self):
        print(f"Producto:{self.nombre}, Categoria:{self.categoria}, Precio:{self.precio}, ID:{self.id}")
        return self
    def __repr__(self) -> str:
        return f"{self.nombre}"