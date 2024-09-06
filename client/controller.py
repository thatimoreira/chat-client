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

def get_message_by_id():
    message_id = input("Informe o ID da mensagem que deseja buscar: ")

    if message_id.isdigit():
       result, status_code  = service.get_message_by_id(int(message_id))

       #print(f"\n\n--->>> DEBUG da lista: {result} <<<---\n")
       #print(f"Tipo: {type(result)}")
       #### result já o  dict que quero, só preciso printar ele ###

       # Se for dict, debugar chaves
       #if isinstance(result, dict):
           #print("Chaves disponíveis: {list(results.keys())}")

       if status_code == 200:
           # Checar se result é um dict com uma chave chamada messages
           if isinstance(result, dict):
               print(f"\nID: {result['id']}")
               print(f"Autor: {result['sender']}")
               print(f"Mensagem: {result['text']}")
               print(f"Data: {result['when']}")
           else:
               print("Não existe mensagem para o ID informado.")
       else:
           print("Erro: {result['error']} (Status: {status_code})")
    else:
        print("ID inválido! Por favor, tente novamente.")
 
def list_all_messages():
    result, status_code = service.get_all_messages()

    if status_code == 200:
        messages = result.get("messages", []) # Acessar messages antes de iterar sobre     as  mensagens
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