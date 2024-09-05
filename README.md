# INFOS importantes
 
 IP do servidor: ```ip-servidor```<br>
 chat está hospedado nele
 
 Comando para consultar (GET) todas as mensagens enviadas:<br>
 curl -sS http://```ip-servidor```/message/0 | jq
 
 Para enviar (POST) uma mensagem:<br>
 curl -X POST -sS http://```ip-servidor```/message/ -d "sender=```nome-de-quem-esta-enviando-a-mensagem```&text=```texto-da-mensagem```" | jq

 <br>
 
 ## Fluxo do client
 
 1. **Usuário interage com o menu**: no arquivo ```app.py```, o usuário escolhe uma opção no menu interativo.<br>
 
 2. **Controller**: recebe as entradas do usuário e chama a função apropriada na **Service**
      Não faz manipulações de dados, apenas direciona a solicitação
       
 3. **Service**: aplica as regras de negócio e validações, então chama o **Repository**<br>
      Não se preocupa com como os dados são armazenados, apenas processa a lógica necessária e passa a responsabilidade para o próximo nível<br>
 
 5. **Repository**: Aqui é onde as operações com dados ocorrem<br>
      Service chama Repository, que faz a comunicação com o servidor utilizando a biblioteca ```requests``` para enviar ou recuperar dados via HTTP<br>
 
 6. **Requisição HTTP**: O servidor responde às requisições HTTP feitas pela Repository<br>
      Repository então processa a resposta e retorna para a **Service**
      Ex: Verifica se a mensagem foi enviada com sucesso
 
 7. **Retorno à Service**: encaminha a resposta processada para a **Controller**<br>
      Service manipula a resposta -> formata para ser melhor exibida para usuário
 
 8. **Retorno à Controller**: exibe o resultado ao usuário<br>
      Exs: Mensagem de sucesso ou a exibição de dados recuperados<br>
 
 9. **Exibição de resultado**<br>
      Controller printa a resposta para o usuário no console<br>
      Fica aguardando nova interação do usuário<br>