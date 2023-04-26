from flask import Flask, make_response, jsonify, request
from bd import Carros

app  = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False 

#Rota da API (Request)
@app.route('/carros', methods = ['GET'] )
def get_carros():
    return make_response(
       jsonify(
            mensagem = 'Lista de carros',
            dados = Carros
        ) 
    )


@app.route('/inserir/carros', methods = ['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso!',
            carro = carro
        )
    )


#Start do servidor
app.run()