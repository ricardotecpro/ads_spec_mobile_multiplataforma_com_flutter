# Quiz 10 - Consumo de APIs REST 📡

1. O que significa a sigla REST?
    - [ ] Real-time Engine Storage Technology.
    - [x] Representational State Transfer.
    - [ ] Remote Essential System Task.
    - [ ] Routing Easy Standard Templates.
    *Explicação: REST é um estilo de arquitetura para sistemas distribuídos, como a web.*

2. Qual protocolo é a base para a comunicação com APIs REST?
    - [ ] FTP
    - [ ] SSH
    - [x] HTTP
    - [ ] SMTP
    *Explicação: Quase todos os serviços web utilizam o protocolo HTTP para troca de dados.*

3. Qual o formato de dados mais utilizado para troca de informações entre o Flutter e um servidor?
    - [ ] XML
    - [ ] CSV
    - [x] JSON
    - [ ] TXT
    *Explicação: O JSON (JavaScript Object Notation) é leve, fácil de ler por humanos e nativamente suportado pelo Dart.*

4. Qual método HTTP usamos para buscar dados de um servidor (ex: lista de produtos)?
    - [ ] POST
    - [x] GET
    - [ ] DELETE
    - [ ] UPDATE
    *Explicação: O `GET` (Obter) é o método padrão para leitura de informações.*

5. Para que serve a palavra-chave `async` em uma função?
    - [ ] Para indicar que a função é secreta.
    - [x] Para indicar que a função realiza operações que levam tempo e retornam um `Future`.
    - [ ] Para deletar a função da memória.
    - [ ] Para acelerar o processador.
    *Explicação: Funções assíncronas permitem que o app continue funcionando enquanto espera por uma resposta da rede.*

6. O que o comando `await` faz dentro de uma função assíncrona?
    - [ ] Encerra a função imediatamente.
    - [x] Pausa a execução da função até que o `Future` seja concluído e devolva o resultado.
    - [ ] Abre um cronômetro na tela.
    - [ ] Reinicia o aplicativo.
    *Explicação: O `await` (aguardar) evita que o código tente usar um dado que ainda não chegou.*

7. Qual classe do Dart representa um valor que estará disponível "no futuro"?
    - [ ] Maybe
    - [ ] Later
    - [x] Future
    - [ ] Pending
    *Explicação: Um `Future<String>` é uma promessa de que você terá uma String daqui a pouco.*

8. Qual a função do método `jsonDecode()`?
    - [ ] Enviar um e-mail.
    - [x] Converter uma String formatada em JSON para um Objeto Dart (como um Map ou List).
    - [ ] Apagar o código JSON.
    - [ ] Traduzir para o português.
    *Explicação: Para acessar os dados (`dados['nome']`), precisamos "decodificar" o texto bruto vindo da API.*

9. O que é um "Status Code 200" em uma resposta HTTP?
    - [ ] Erro interno do servidor.
    - [ ] Página não encontrada.
    - [x] Sucesso (OK).
    - [ ] Acesso negado.
    *Explicação: O código 200 indica que a requisição foi processada com sucesso.*

10. E o famoso "Erro 404"?
    - [ ] Sucesso total.
    - [ ] Problema no banco de dados.
    - [x] Recurso não encontrado (Not Found).
    - [ ] Sem conexão com a internet.
    *Explicação: Significa que a URL digitada não existe no servidor.*
