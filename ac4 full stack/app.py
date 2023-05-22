from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Conectando ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco_de_dados"
)


@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()

    results = []
    for usuario in usuarios:
        usuario_data = {
            'id': usuario[0],
            'nome': usuario[1],
            'email': usuario[2]
        }
        results.append(usuario_data)

    return jsonify(results)


@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    data = request.get_json()
    nome = data['nome']
    email = data['email']

    cursor = db.cursor()
    query = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    values = (nome, email)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return jsonify({'message': 'Usuário adicionado com sucesso'})


if __name__ == '__main__':
    app.run()
