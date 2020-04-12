from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'Nome': 'Tiago', 'Habilidades': ['Python', 'Django']},
    {'Nome': 'Chaves', 'Habilidades': ['Python', 'Flask']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não foi encontrado'.format(id)
            response = {"Status": "Erro!", "Mensagem": mensagem}
        except Exception:
            mensagem = 'Erro Desconhecido, favor entrar em contato com o Desenvolvedor'
            response = {"Status": "Desconhecido", "mensagem": mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"Status": "Id {} excluido.".format(id)}


class listaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return {"Status": "id {} criado com sucesso".format(posicao)}

api.add_resource(Desenvolvedor, '/<int:id>')
api.add_resource(listaDesenvolvedores, '/')
api.add_resource(Habilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)