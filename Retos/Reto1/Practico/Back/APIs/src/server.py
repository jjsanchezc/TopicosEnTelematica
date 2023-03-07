from flask import Flask, request, jsonify
from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc
import inventory_service_pb2_grpc
import inventory_service_pb2
import multiprocessing

app = Flask(__name__)

# Configuración de los endpoints de los microservicios
inventory_channel = 'localhost:50051'
shoppingcart_channel = 'localhost:50052'

# Creación de los canales de comunicación para cada microservicio
inventory_port = grpc.insecure_channel(inventory_channel)
shoppingcart_port = grpc.insecure_channel(shoppingcart_channel)

# Creación de los stubs para cada microservicio
inventory_stub = inventory_service_pb2_grpc.ProductAvailabilityStub(inventory_port)
shoppingcart_stub = shopping_cart_service_pb2_grpc.ProductServiceStub(shoppingcart_port)

@app.route('/ProductToSearch', methods=['POST'])
def inventory():
    # store the postman request
    data = request.json
    
    ans=inventory_stub.SearchProduct(inventory_service_pb2.ProductToSearch(id_product=int(data["id_product"])))
    if ans.status_code==True:
        return "Se agregó correctamente el producto "+ str(data["id_product"])
    else:
        return "No hay stock del producto "+ str(data["id_product"])

@app.route('/ShoppingCartService/AddProduct', methods=['POST'])
def shoppingcart_addproduct():
    # store the postman request
    data = request.json
    sc=shoppingcart_stub.AddProduct(shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=int(data["id_product"])))
    print(str(sc.status_code)+"este es el status code")
    if sc.status_code==0:
        return f"No se pudo añadir el producto {str(data['id_product'])} ya que no hay stock del producto "
    else:
        return f"Se añadió correctamente el producto {str(data['id_product'])} al carrito"

@app.route('/ShoppingCartService/DeleteProduct', methods=['POST'])
def shoppingcart_deleteproduct():
    # store the postman request
    data = request.json
    try:
        sc=shoppingcart_stub.DeleteProduct(shopping_cart_service_pb2.DeleteProductFromCart(id_product=int(data["id_product"]),reason=str(data["reason"])))
    except:
        sc=shoppingcart_stub.DeleteProduct(shopping_cart_service_pb2.DeleteProductFromCart(id_product=int(data["id_product"])))
    if sc.status_code==0:
        return f"No se pudo eliminar el producto {str(data['id_product'])} ya que no lo tenias en el carrito"
    else:
        return f"Se eliminó correctamente el producto {str(data['id_product'])} al carrito y te quedan {str(sc.product_quantity_left)} del mismo producto en el carrito"


if __name__ == '__main__':
    app.run(debug=True)
