# Exibe menu e passa para a Controller de acordo com opção escolhida pelo usuário

from client import controller

def menu():
    valid_options = {'1', '2', '3', '4', '5', '6', '7', '8'}

    while True:
        print("\n-------------- MENU --------------")
        print("1. Enviar mensagem")
        print("2. Exibir mensagens não lidas")
        print("3. Exibir mensagem por autor(a)")
        print("4. Exibir mensagem por ID")
        print("5. Exibir todas as mensagens")
        print("6. Editar mensagem")
        print("7. Deletar mensagem")
        print("8. Sair")

        user_option = input("\nOpção: ")

        if user_option not in valid_options:
            print("\nOpção inválida!\nPor favor, digite um número entre 1 e 8")
        else:
            if user_option == '1':
                controller.create_message()
            elif user_option == '2':
                #controller.list_unread_messages()
                print("Mensagens NÃO LIDAS")
            elif user_option == '3':
                #controller.list_messages_by_author()
                print("Mensagens POR AUTOR")
            elif user_option == '4':
                #controller.get_message_by_id()
                print("Mensagens POR ID")
            elif user_option == '5':
                controller.list_all_messages()
            elif user_option == '6':
                #controller.edit_message()
                print("EDITAR mensagem")
            elif user_option == '7':
                #controller.delete_message()
                print("APAGAR mensagem")
            elif user_option == '8':
                print("Chat encerrado")
                break
 
if __name__ == "__main__":
    menu()
