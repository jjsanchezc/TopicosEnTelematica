from flask import Flask, jsonify, request
from user import User

app = Flask(__name__)

messages_queue = []
username='JJ'   


#FIRTS ALL PUBLISHER METHODS
@app.route('/mensaje/<topic_name>', methods=['POST'])
def send_message(topic_name):
    user=User(username)
    user.add_topic_pub(topic_name)
    if not user.send_message(topic_name):
        return jsonify({'mensaje': 'Error al enviar, topico no existe','a': str(user.my_topics_pub)})
    else:
        message=request.json['mensaje']
        add_queue(message)
        return jsonify({'mensaje': 'Mensaje enviado correctamente'})

def add_queue(mensaje):
    messages_queue.append(mensaje)


class MessageBroker:
    def __init__(self,nombre_topico,mensaje,) -> None:
        self.exchange=self.Exchange()
        self.queue=self.Queue()
    
    class Exchange:
        def __init__(self) -> None:
            pass
        
        def get_topics(self):
            pass
    
    
    class Queue:
        '''la cola almacena y luego entrega los mensajes a cada consumir
        '''        
        def __init__(self) -> None:
            pass
        