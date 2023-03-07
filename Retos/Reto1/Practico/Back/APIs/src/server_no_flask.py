#este deberia estar en la branch nueva
from concurrent import futures
import logging
import grpc
import shopping_cart_service_pb2
import shopping_cart_service_pb2_grpc
import inventory_service_pb2_grpc
import inventory_service_pb2
import multiprocessing

HOST = 'localhost:3000'

class ProductService(shopping_cart_service_pb2_grpc.ProductServiceServicer):
    def AddProduct(self, request, context):
        '''In this method, user send the number id of the product they want to add to their shopping carr

        Args:
            request (_type_): this is the product id they want to add to the shopping cart
            context (_type_): this is used by gRPC

        Returns:
            _type_: There are 2 ways of return, product added to the shopping cart or product out of stock and couldn't add it 
        '''
        with grpc.insecure_channel('localhost:50052') as channel:
            stub =  shopping_cart_service_pb2_grpc.ProductServiceStub(channel)
            try:
                stub.AddProduct(shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=request.id_product))
                print('Producto añadido:\n ' + str(request))
            except:
                print('no se pudo añadir al carrito')
        return shopping_cart_service_pb2.ProductAdditionToCartResponse(status_code=1)


#TODAVIA SIGUE MANDANDO SOLO EL 1
class ProductAvailability(inventory_service_pb2_grpc.ProductAvailabilityServicer):
    def SearchProduct(self, request, context):
        print('este es el request que le entra '+ str(request.id_product))
        with grpc.insecure_channel('localhost:50051') as channel:
            stub =  inventory_service_pb2_grpc.ProductAvailabilityStub(channel)
            
            ans=stub.SearchProduct(inventory_service_pb2.ProductToSearch(id_product=request.id_product))
            if ans.status_code == True:
                print(f'Producto {str(request)} Encontrado')
            else:
                print('no hay se encuentra disponible')
        
        return inventory_service_pb2.ProductAvailabilityResponse(status_code=1)

def serve():
    # First, the user have to define if he wants to shearch for stock or add to the shoppingcart
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    #Add shoppingcart to server
    shopping_cart_service_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), servidor)
    
    #Add Inventory to server
    inventory_service_pb2_grpc.add_ProductAvailabilityServicer_to_server(ProductAvailability(), servidor)
    
    print('APIs Server running')
    servidor.add_insecure_port(HOST)
    servidor.start()
    servidor.wait_for_termination()


if __name__ == "__main__":
    serv = multiprocessing.Process(target=serve)
    serv.start()
