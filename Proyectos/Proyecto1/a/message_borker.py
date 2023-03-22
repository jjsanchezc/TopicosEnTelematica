from flask import Flask, jsonify, request

app = Flask(__name__)

mensajes = []

# ruta para enviar un mensaje
@app.route('/mensaje', methods=['POST'])
def enviar_mensaje():
    mensaje = request.json['mensaje']
    mensajes.append(mensaje)
    return jsonify({'mensaje': 'Mensaje enviado correctamente'})

# ruta para recibir todos los mensajes
@app.route('/mensaje', methods=['GET'])
def recibir_mensajes():
    return jsonify({'mensajes': mensajes})

if __name__ == '__main__':
    app.run(debug=True)
