# Quiz 10 - Consumo de APIs REST 📡

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que significa a sigla REST?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. REST é um estilo de arquitetura para sistemas distribuídos, como a web.">Real-time Engine Storage Technology.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! REST é um estilo de arquitetura para sistemas distribuídos, como a web.">Representational State Transfer.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. REST é um estilo de arquitetura para sistemas distribuídos, como a web.">Remote Essential System Task.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. REST é um estilo de arquitetura para sistemas distribuídos, como a web.">Routing Easy Standard Templates.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual protocolo é a base para a comunicação com APIs REST?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase todos os serviços web utilizam o protocolo HTTP para troca de dados.">FTP</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase todos os serviços web utilizam o protocolo HTTP para troca de dados.">SSH</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quase todos os serviços web utilizam o protocolo HTTP para troca de dados.">HTTP</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase todos os serviços web utilizam o protocolo HTTP para troca de dados.">SMTP</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual o formato de dados mais utilizado para troca de informações entre o Flutter e um servidor?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JSON (JavaScript Object Notation) é leve, fácil de ler por humanos e nativamente suportado pelo Dart.">XML</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JSON (JavaScript Object Notation) é leve, fácil de ler por humanos e nativamente suportado pelo Dart.">CSV</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O JSON (JavaScript Object Notation) é leve, fácil de ler por humanos e nativamente suportado pelo Dart.">JSON</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JSON (JavaScript Object Notation) é leve, fácil de ler por humanos e nativamente suportado pelo Dart.">TXT</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual método HTTP usamos para buscar dados de um servidor (ex: lista de produtos)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `GET` (Obter) é o método padrão para leitura de informações.">POST</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `GET` (Obter) é o método padrão para leitura de informações.">GET</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `GET` (Obter) é o método padrão para leitura de informações.">DELETE</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `GET` (Obter) é o método padrão para leitura de informações.">UPDATE</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve a palavra-chave `async` em uma função?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções assíncronas permitem que o app continue funcionando enquanto espera por uma resposta da rede.">Para indicar que a função é secreta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Funções assíncronas permitem que o app continue funcionando enquanto espera por uma resposta da rede.">Para indicar que a função realiza operações que levam tempo e retornam um `Future`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções assíncronas permitem que o app continue funcionando enquanto espera por uma resposta da rede.">Para deletar a função da memória.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções assíncronas permitem que o app continue funcionando enquanto espera por uma resposta da rede.">Para acelerar o processador.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que o comando `await` faz dentro de uma função assíncrona?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `await` (aguardar) evita que o código tente usar um dado que ainda não chegou.">Encerra a função imediatamente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `await` (aguardar) evita que o código tente usar um dado que ainda não chegou.">Pausa a execução da função até que o `Future` seja concluído e devolva o resultado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `await` (aguardar) evita que o código tente usar um dado que ainda não chegou.">Abre um cronômetro na tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `await` (aguardar) evita que o código tente usar um dado que ainda não chegou.">Reinicia o aplicativo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual classe do Dart representa um valor que estará disponível "no futuro"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um `Future<String>` é uma promessa de que você terá uma String daqui a pouco.">Maybe</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um `Future<String>` é uma promessa de que você terá uma String daqui a pouco.">Later</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um `Future<String>` é uma promessa de que você terá uma String daqui a pouco.">Future</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um `Future<String>` é uma promessa de que você terá uma String daqui a pouco.">Pending</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a função do método `jsonDecode()`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para acessar os dados (`dados['nome']`), precisamos "decodificar" o texto bruto vindo da API.">Enviar um e-mail.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Para acessar os dados (`dados['nome']`), precisamos "decodificar" o texto bruto vindo da API.">Converter uma String formatada em JSON para um Objeto Dart (como um Map ou List).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para acessar os dados (`dados['nome']`), precisamos "decodificar" o texto bruto vindo da API.">Apagar o código JSON.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para acessar os dados (`dados['nome']`), precisamos "decodificar" o texto bruto vindo da API.">Traduzir para o português.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O que é um "Status Code 200" em uma resposta HTTP?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O código 200 indica que a requisição foi processada com sucesso.">Erro interno do servidor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O código 200 indica que a requisição foi processada com sucesso.">Página não encontrada.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O código 200 indica que a requisição foi processada com sucesso.">Sucesso (OK).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O código 200 indica que a requisição foi processada com sucesso.">Acesso negado.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. E o famoso "Erro 404"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Significa que a URL digitada não existe no servidor.">Sucesso total.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Significa que a URL digitada não existe no servidor.">Problema no banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Significa que a URL digitada não existe no servidor.">Recurso não encontrado (Not Found).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Significa que a URL digitada não existe no servidor.">Sem conexão com a internet.</div>
  <div class="quiz-feedback"></div>
</div>
