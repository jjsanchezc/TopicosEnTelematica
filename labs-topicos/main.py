import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('34.239.192.132', 5672, '/',pika.PlainCredentials('user', 'password')))
channel = connection.channel()
channel.basic_publish(exchange='my_exchange', routing_key='test', body='Test!')
print("Runnning Producer Application...")
print(" [x] Sent 'Hello World...!'")
connection.close()