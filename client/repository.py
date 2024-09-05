# Acessa os dados
# Interage com os dados

# Faz requisições HTTP para server
# Funções para fazer requisições GET e POST

import requests

API_URL = "http://192.168.1.9:8080/"

def save_message(message):
    response = requests.post(API_URL + "message", data=message)

    if response.status_code == 201:
        return response.json(), 201
    return {"erro": "Falha ao salvar mensagem"}, response.status_code