#este metodo luego se va a GO

from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc

import inventory_shopping_cart_service_pb2_grpc
import inventory_shopping_cart_service_pb2

def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub =  shopping_cart_service_pb2_grpc.ProductServiceStub(channel)
        producto_id=int(input('por favor seleccione el producto del 1-10\n'))
        try:
            stub.AddProduct(shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=producto_id))
        except:
            print('a')
    

if __name__ == '__main__':
    logging.basicConfig()
    run()