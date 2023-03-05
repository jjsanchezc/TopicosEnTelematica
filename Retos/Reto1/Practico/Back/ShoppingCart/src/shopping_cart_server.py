from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc

import inventory_shopping_cart_service_pb2_grpc
import inventory_shopping_cart_service_pb2
import multiprocessing


HOST1 = '[::]:8080'

class ProductService(shopping_cart_service_pb2_grpc.ProductServiceServicer):
    def AddProduct(self, request, context):
        print('Producto añadido:\n ' + str(request))
        return shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=1)


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
    
    
    
'''
    inventory_connection=multiprocessing.Process(target=inventory_server)
    inventory_connection.start()
    
class ProductAvailability(inventory_shopping_cart_service_pb2_grpc.ProductAvailabilityServicer):
    def SearchProduct(self,request,context):
        print('producto a buscar:\n '+ str(request))
        return inventory_shopping_cart_service_pb2.ProductAvailabilityResponse(status_code=1,availability=2)

def inventory_server():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_shopping_cart_service_pb2_grpc.add_ProductAvailabilityServicer_to_server(
        ProductAvailability(), servidor)
    servidor.add_insecure_port(HOST2)
    print('Service2 is Running')
    servidor.start()
    servidor.wait_for_termination()
'''