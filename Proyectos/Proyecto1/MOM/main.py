from flask import Flask, jsonify, redirect, request
from client import Client

app = Flask(__name__)

messages_queue = []
user='JJ'   
@app.route('/login', methods=['POST'])
def home_login():
    '''home page, where the user will log in

    Returns:
        returns the "page" where the user will select if they want to be publisher or subscriber
    '''  
    return redirect("localhost:5000/menu_choice/")

@app.route('/menu_choice', methods=['POST'])
def menu_choice():
    choice=request
    if choice=='1':
        #go to publisher
        pass
    elif choice=='2':
        #go to subscriber
        pass
    else:
        return redirect("localhost:5000/menu_choice/")
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
