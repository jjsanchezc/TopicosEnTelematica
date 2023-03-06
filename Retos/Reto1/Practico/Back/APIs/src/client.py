#este metodo luego se va a GO

from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc

import inventory_service_pb2_grpc
import inventory_service_pb2

def run():
    option=input('quieres agregar al carro (opcion 1) o buscar en el inventario (opcion 2) ?')
    with grpc.insecure_channel('localhost:3000') as channel:
        if option=="1":
            stub =  shopping_cart_service_pb2_grpc.ProductServiceStub(channel)
            producto_id=int(input('por favor seleccione el producto del 1-10\n'))
            try:
                stub.AddProduct(shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=producto_id))
            except:
                print('ERROR EN EL CLIENTE')
        else:
            stub =  inventory_service_pb2_grpc.ProductAvailabilityStub(channel)
            producto_id=int(input('por favor seleccione el producto a buscar del 1-10\n'))
            try:
                stub.SearchProduct(inventory_service_pb2.ProductAvailabilityResponse(status_code=3))
            except:
                print('ERROR EN EL CLIENTE')
    

if __name__ == '__main__':
    logging.basicConfig()
    run()