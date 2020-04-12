from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'Nome': 'Tiago',
        'Habilidades': [
            'Python', 'Django'
        ]
     },
    {
        'Nome': 'Chaves',
        'Habilidades': [
            'Python', 'Flask'
        ]
     }
]


@app.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não foi encontrado'.format(id)
            response = {"Status": "Erro!", "Mensagem": mensagem}
        except Exception:
            mensagem = 'Erro Desconhecido, favor entrar em contato com o Desenvolvedor'
            response = {"Status": "Desconhecido", "mensagem": mensagem}

        return jsonify(response)
    if request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    if request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"Status": "ID {} Excluido com sucesso".format(id)})

@app.route('/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify({"Status": "id {} Criado com sucesso".format(posicao)})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)