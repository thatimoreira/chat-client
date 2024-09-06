# Regras de negócio, validações e chama Repository, que faz operações com os dados

from client import repository

def create_message(data):
    sender = data.get('sender')
    text = data.get('text')

    message = { 
        "sender": sender,
        "text": text
    }   

    return repository.save_message(message)

def get_message_by_id(message_id):
    result, status_code = repository.fetch_message_by_id(message_id)

    # Solução temporária para filtrar por id
    # Motivo: problema no endpoint que retorna várias mensagens ao consultar um id
    if status_code == 200 and isinstance(result, dict):
        messages = result.get('messages', []) 
        for message in messages:
            if message.get('id')  == message_id:
                return message, 200 
    return {"error": "Mensagem não encontrada"}, 404 

def get_all_messages():
    messages, status_code = repository.fetch_all_messages()

    return messages, status_code