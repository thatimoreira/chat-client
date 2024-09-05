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

def get_all_messages():
    messages, status_code = repository.fetch_all_messages()

    return messages, status_code