from flask_restful import Resource, request
import json

lista_habilidades = ['Python', 'Java', 'Django', 'Flask', 'PHP']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return lista_habilidades


class Habilidade(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Habilidade nao encontrada'
            response = {"Status": mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, contactar administrador'
            response = {"Status": mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return {'Status': "{} Alterado com sucesso".format(id)}

    def delete(self, id):
        lista_habilidades.pop(id)
        return {"Status": "Id {} deletado com sucesso".format(id)}