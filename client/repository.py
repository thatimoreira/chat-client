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

def fetch_message_by_id(message_id):
    # Solução temporária para filtrar por id (subtração de uma unidade do id passado no    request)
    # Motivo: problema no endpoint que retorna várias mensagens ao consultar um id
    response = requests.get(f"{API_URL}/message/{message_id - 1}")

    if response.status_code == 200:
        return response.json(), 200 
    return {"error": "Mensagem não encontrada"}, response.status_code

def fetch_all_messages():
    response = requests.get(API_URL + "message/0")

    if response.status_code == 200:
        return response.json(), 200 
    return {"erro": "Falha ao pesquisar mensagens"}, response.status_code