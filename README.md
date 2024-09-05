# INFOS importantes
 
 IP do servidor: ```ip-servidor```<br>
 chat está hospedado nele
 
 Comando para consultar (GET) todas as mensagens enviadas:<br>
 curl -sS http://```ip-servidor```/message/0 | jq
 
 Para enviar (POST) uma mensagem:<br>
 curl -X POST -sS http://```ip-servidor```/message/ -d "sender=```nome-de-quem-esta-enviando-a-mensagem```&text=```texto-da-mensagem```" | jq

 <br>
 
 ## Fluxo do client
 
 1. **Usuário interage através de um menu**<br>
    Input do usuário é passado para a controller
 
 2. **Controller chama Service**<br>
    Controller chama a função da Service de acordo com a opção escolhida pelo usuário no menu interativo<br>
    - Obs: Não manipula dados ou faz validações, somente direciona para o serviço correto
       
 3. **Service aplica as regras de negócio**<br>
    Recebe a requisição da Controller<br>
    Aplica as regras de negócio<br>
    Não se preocupa em como os dados serão armazenados e recuperados (quem faz isso é a Repository)<br>
 
 4. **Service chama a Repository**<br>
    Depois de aplicar as regras de negócio, Service chama a Repository para fazer operações com dados]
    Ex: chamar função para de fato enviar a mensagem para o server
 
 5. **Repository faz requisições HTTP para server**<br>
    Usa a lib requests para fazer requisições HTTP
    Ex: faz requisição POST para salvar nova mensagem no server

    Recebe resposta do server com confirmação de que a mensagem foi criada com sucesso (??? )
 
 6. **Repository passa a resposta para a Service**<br>
     Envia para a Service a confirmação sobre o status da criação da mensagem ou dados da mensagem consultada
    Service manipula a resposta -> formata para ser melhor exibida para usuário
 
 7. **Service encaminha a resposta para a Controller**<br>
    Retorna os dados processados para a Controller<br>
    Informa se a operação foi bem sucedida junto com dados relevantes (ex: status da operação, lista de mensagens)<br>
 
 8. **Controller mostra o resultado para usuário**<br>
    Pode ser uma mensagem de sucesso ou lista de mensagens (como "Mensagem enviada com sucesso!") consultadas no server<br>
    Fica aguardando nova interação do usuário<br>
