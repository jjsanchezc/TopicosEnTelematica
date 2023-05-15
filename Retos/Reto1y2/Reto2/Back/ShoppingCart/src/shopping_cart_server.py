  GNU nano 6.2                                                                                                                     shopping_cart_server.py                                                                                                                              from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc

import inventory_shopping_cart_service_pb2_grpc
import inventory_shopping_cart_service_pb2
import multiprocessing


HOST1 = '54.147.224.238:5000'

class ProductService(shopping_cart_service_pb2_grpc.ProductServiceServicer):
    def AddProduct(self, request, context):
        print('recibi el pedido')
        with grpc.insecure_channel('54.147.224.238:50051') as channel:
            stub2 =inventory_shopping_cart_service_pb2_grpc.ProductAvailabilityStub(channel)
            product_available=stub2.SearchProduct(inventory_shopping_cart_service_pb2.ProductToSearch(id_product=request.id_product))
        if product_available.status_code==False:
            print('No hay mas stock')
            return shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=False)
        else:
            print('Producto añadido:\n ' + str(request))
            return shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=True)

    def DeleteProduct(self, request, context):
        print('recibi orden para eliminar del carrito al producto', str(request.id_product))
        if str(request.reason)!="":
            print(f'razón del cliente: "{str(request.reason)}"')
        if request.id_product==1 or request.id_product==2:
            print('no tienes este producto en tu carro')
            return shopping_cart_service_pb2.ProductDeletedInCartResponse(status_code=False,id_product=request.id_product,product_quantity_left=0)
        else:
            return shopping_cart_service_pb2.ProductDeletedInCartResponse(status_code=True,id_product=request.id_product,product_quantity_left=2)

def server():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shopping_cart_service_pb2_grpc.add_ProductServiceServicer_to_server(
        ProductService(), servidor)
    servidor.add_insecure_port(HOST1)
    print('Service1 is Running')
    servidor.start()
    servidor.wait_for_termination()



if __name__ == "__main__":
    serv = multiprocessing.Process(target=server)
    serv.start()