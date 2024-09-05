# É o "meio de campo" entre o usuário e os serviços (que fazem requisições HTTP)

# Lida com as requests e responses
# "Decide" quais funções serão executadas (encaminha para  a Service executar)
# Devolve as respostas para usuário

from client import service

def create_message():
    sender = input("Login: ")
    text = input("Mensagem: ")
    result, status_code = service.create_message({"sender": sender, "text": text})
    print(result, f"Status: {status_code}")

def list_all_messages():
    result, status_code = service.get_all_messages()

    if status_code == 200:
        messages = result.get("messages", []) # Acessar messages antes de iterar sobre as  mensagens
        for message in messages:
            if isinstance(message, dict):
                print(f"ID: {message['id']}")
                print(f"Autor: {message['sender']}")
                print(f"Mensagem: {message['text']}")
                print(f"Data: {message['when']}")
            else:
                print("Mensagem com formato inválido!")
    else:
        print(f"Erro ao consultar mensagens.\nStatus: {status_code}")