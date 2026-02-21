# Quiz 07 - Navegação entre Telas 🛣️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual classe é responsável por gerenciar a pilha de telas no Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Navigator` controla a transição e a memória das telas visitadas.">ScreenManager</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `Navigator` controla a transição e a memória das telas visitadas.">Navigator</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Navigator` controla a transição e a memória das telas visitadas.">Router</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Navigator` controla a transição e a memória das telas visitadas.">StackController</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que o comando `Navigator.push()` faz?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Puxar (push) uma tela significa colocá-la na frente do usuário.">Deleta a tela atual.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Puxar (push) uma tela significa colocá-la na frente do usuário.">Adiciona uma nova tela ao topo da pilha de navegação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Puxar (push) uma tela significa colocá-la na frente do usuário.">Reinicia o aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Puxar (push) uma tela significa colocá-la na frente do usuário.">Fecha o aplicativo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Como voltamos para a tela anterior programaticamente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `pop` retira o prato (tela) do topo da pilha, revelando o que estava embaixo.">Navigator.back(context)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O comando `pop` retira o prato (tela) do topo da pilha, revelando o que estava embaixo.">Navigator.pop(context)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `pop` retira o prato (tela) do topo da pilha, revelando o que estava embaixo.">Navigator.remove(context)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `pop` retira o prato (tela) do topo da pilha, revelando o que estava embaixo.">context.goBack()</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que é uma "Rota Nomeada"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Rotas nomeadas facilitam a organização em aplicativos que possuem muitas telas.">Uma foto da tela.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Rotas nomeadas facilitam a organização em aplicativos que possuem muitas telas.">Uma String que identifica uma tela de forma única (ex: '/login').</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Rotas nomeadas facilitam a organização em aplicativos que possuem muitas telas.">O nome do autor do código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Rotas nomeadas facilitam a organização em aplicativos que possuem muitas telas.">Um tipo de botão.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Onde definimos o mapa de rotas nomeadas de um aplicativo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialApp` centraliza a configuração de navegação do projeto.">No Scaffold.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `MaterialApp` centraliza a configuração de navegação do projeto.">No MaterialApp (parâmetro routes).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialApp` centraliza a configuração de navegação do projeto.">No arquivo pubspec.yaml.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialApp` centraliza a configuração de navegação do projeto.">Dentro do método build de cada tela.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual widget é usado para criar a transição visual padrão entre telas no Android e iOS?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialPageRoute` adapta a animação de entrada conforme o sistema operacional (subida no iOS, fade no Android).">BoxRoute</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialPageRoute` adapta a animação de entrada conforme o sistema operacional (subida no iOS, fade no Android).">CustomRoute</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `MaterialPageRoute` adapta a animação de entrada conforme o sistema operacional (subida no iOS, fade no Android).">MaterialPageRoute</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialPageRoute` adapta a animação de entrada conforme o sistema operacional (subida no iOS, fade no Android).">AppRoute</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como passamos dados de uma tela para outra de forma simples?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Passar argumentos via construtor é a forma mais direta e segura de transferir informações.">Salvando em um arquivo de texto.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Passar argumentos via construtor é a forma mais direta e segura de transferir informações.">Através do construtor da classe da nova tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Passar argumentos via construtor é a forma mais direta e segura de transferir informações.">Usando o comando `sendData()`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Passar argumentos via construtor é a forma mais direta e segura de transferir informações.">Não é possível passar dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que acontece se chamarmos `Navigator.pop()` na única tela do app?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem nada abaixo na pilha, o pop retira a última instância e encerra o processo visual.">O app mostra um erro fatal.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem nada abaixo na pilha, o pop retira a última instância e encerra o processo visual.">Nada acontece.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem nada abaixo na pilha, o pop retira a última instância e encerra o processo visual.">O aplicativo geralmente é encerrado (fechado).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem nada abaixo na pilha, o pop retira a última instância e encerra o processo visual.">O app volta para a tela de boot.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual a diferença entre `push` e `pushReplacement`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para telas de Login ou Splash Screens onde você não quer que o usuário volte ao clicar em "Voltar".">Nenhuma, são sinônimos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para telas de Login ou Splash Screens onde você não quer que o usuário volte ao clicar em "Voltar".">`pushReplacement` é mais lento.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Útil para telas de Login ou Splash Screens onde você não quer que o usuário volte ao clicar em "Voltar".">`pushReplacement` substitui a tela atual na pilha em vez de apenas empilhar por cima.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para telas de Login ou Splash Screens onde você não quer que o usuário volte ao clicar em "Voltar".">`pushReplacement` apaga o banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como definimos qual tela será a primeira a abrir no app usando rotas?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `initialRoute` define o ponto de partida do fluxo de navegação.">Parâmetro `start:`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `initialRoute` define o ponto de partida do fluxo de navegação.">Parâmetro `home:`.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `initialRoute` define o ponto de partida do fluxo de navegação.">Parâmetro `initialRoute:`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `initialRoute` define o ponto de partida do fluxo de navegação.">Parâmetro `first:`.</div>
  <div class="quiz-feedback"></div>
</div>
