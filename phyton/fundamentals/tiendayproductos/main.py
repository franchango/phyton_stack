from tienda import Tienda
from producto import Producto

tienda_1 = Tienda("La Vuelta")

arroz = Producto("Arroz",45,"Alimentos",15)
leche = Producto("leche",1.20,"Lacteos",56)
mantequilla = Producto("Mantequilla",3.50,"Lacteos",1.56)
yoghurt = Producto("Yoghurt",4.50,"Lacteos",8.75)


tienda_1.add_product(arroz).add_product(leche).add_product(mantequilla).add_product(yoghurt).print_tienda()

tienda_1.sell_product(2).print_tienda()

tienda_1.inflation(5).print_tienda()

tienda_1.set_clearance("Lacteos", 10).print_tienda()

tienda_1.sell_product_id(875).print_tienda()
print(tienda_1.lista_productos)
#import pdb; pdb.set_trace()