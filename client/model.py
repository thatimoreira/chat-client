# Padronizção da estrutura das mensagens (recebidas e enviadas)

# validar
# processar
# formatar

# Define como os dados são armazenados e manipulados
# Converte para JSON

def create_message(sender, text, msg_ID=None):
    return {
        "id" : msg_ID,
        "sender": sender,
        "text": text
    }