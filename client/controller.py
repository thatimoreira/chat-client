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