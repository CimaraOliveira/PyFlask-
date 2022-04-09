from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#crinado lista de desenvolvedores exemplo de caminho http://127.0.0.1:5000/dev/1/
desenvolvedores = [
    {
        'id':'0',
        'nome':'cimara',
        'habilidades': ['python', 'django']
     },
    {
        'id':'1',
        'nome':'Guilherme',
        'habilidades': ['java', 'spring']
    }
]
#mtodos de get, put e delete
@app.route('/dev/<int:id>/', method=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
        if request.method == 'GET':
            try:
                response = desenvolvedores[id]
            except IndexError:
                mensagem = 'Desenvolvedor de id {} não existe'.format(id)
                response = {'status': 'erro', 'mensagem': mensagem}
            except Exception:
                mensagem = 'Erro desconhecido!'
                response = {'status': 'erro', 'mensagem': mensagem}
            return jsonify(response)
        elif request.method == 'PUT':
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)
        elif request.method == 'DELETE':
            desenvolvedores.pop(id)
            return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido com sucesso!'})

#adiciona e lista todos os desenvolvedores
@app.route('/dev/', method=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__=="__main__":
    app.run(debug=True)

