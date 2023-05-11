#este metodo luego se va a GO

from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc

import inventory_service_pb2_grpc
import inventory_service_pb2

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub =  shopping_cart_service_pb2_grpc.ProductServiceStub(channel)
        producto_id=int(input('por favor seleccione el producto del 1-10\n'))
        
        #Starts connection with Inventory (CREO QUE ES EL API)
        with grpc.insecure_channel('localhost:50051') as channel:
            stub2 =inventory_service_pb2_grpc.ProductAvailabilityStub(channel)
            product_available=stub2.SearchProduct(inventory_service_pb2.ProductToSearch(id_product=producto_id))

        if product_available.status_code==False:
            print('No hay mas stock')
        else:
            stub.AddProduct(shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=producto_id))
            print("Agregado Correctamente ")
    

if __name__ == '__main__':
    logging.basicConfig()
    run()