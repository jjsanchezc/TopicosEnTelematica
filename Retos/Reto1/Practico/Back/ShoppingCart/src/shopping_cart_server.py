from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc

import inventory_shopping_cart_service_pb2_grpc
import inventory_shopping_cart_service_pb2
import multiprocessing


HOST1 = '[::]:50052'

class ProductService(shopping_cart_service_pb2_grpc.ProductServiceServicer):
    def AddProduct(self, request, context):
        print('recibi el pedido')
        with grpc.insecure_channel('localhost:50051') as channel:
            stub2 =inventory_shopping_cart_service_pb2_grpc.ProductAvailabilityStub(channel)
            product_available=stub2.SearchProduct(inventory_shopping_cart_service_pb2.ProductToSearch(id_product=request.id_product))
            print(product_available.status_code)
        if product_available.status_code==False:
            print('No hay mas stock')
            return shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=False)
        else:
            print('Producto añadido:\n ' + str(request))
            return shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=True)


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