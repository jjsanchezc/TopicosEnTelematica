from flask import Flask, jsonify, request
from client import Client

app = Flask(__name__)

messages_queue = []
user='JJ'   
#FIRTS ALL PUBLISHER METHODS
@app.route('/mensaje/<topic_name>', methods=['POST'])
def send_message(topic_name):
    client=Client(user)
    client.add_topic_pub(topic_name)
    if not client.send_message(topic_name):
        return jsonify({'mensaje': 'Error al enviar, topico no existe','a': str(client.my_topics_pub)})
    else:
        message=request.json['mensaje']
        add_queue(message)
        return jsonify({'mensaje': 'Mensaje enviado correctamente'})

def add_queue(mensaje):
    messages_queue.append(mensaje)





#SECOND ALL THE SUBSCRIBER METHODS
# Ruta para recibir un mensaje
@app.route('/mensaje', methods=['GET'])
def recibir_mensaje():
    if len(messages_queue) == 0:
        return jsonify({'mensaje': 'No hay mensajes'})
    else:
        mensaje = messages_queue.pop(0)
        return jsonify({'mensaje': mensaje})






if __name__ == '__main__':
    app.run(debug=True)
