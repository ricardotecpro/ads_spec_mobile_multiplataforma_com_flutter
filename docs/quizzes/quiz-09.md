# Quiz 09 - Gerenciamento de Estado 🔄

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é "Estado" no Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estado é a "memória" do app: um contador, se um botão está ativo, ou dados de um usuário logado.">O país onde o desenvolvedor mora.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Estado é a "memória" do app: um contador, se um botão está ativo, ou dados de um usuário logado.">Dados que podem mudar e que afetam o que é exibido na tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estado é a "memória" do app: um contador, se um botão está ativo, ou dados de um usuário logado.">O tamanho do arquivo do aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estado é a "memória" do app: um contador, se um botão está ativo, ou dados de um usuário logado.">O ícone da bateria do celular.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual o comando básico para atualizar a tela em um StatefulWidget?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `setState` avisa ao Flutter que os dados mudaram e que o método `build` precisa rodar de novo.">refresh()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `setState` avisa ao Flutter que os dados mudaram e que o método `build` precisa rodar de novo.">updateUI()</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `setState` avisa ao Flutter que os dados mudaram e que o método `build` precisa rodar de novo.">setState()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `setState` avisa ao Flutter que os dados mudaram e que o método `build` precisa rodar de novo.">reload()</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Por que o `setState()` não é recomendado para aplicativos grandes e complexos?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciadores de estado globais (como Provider) são necessários para manter o código organizado quando o app cresce.">Porque ele apaga o banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciadores de estado globais (como Provider) são necessários para manter o código organizado quando o app cresce.">Porque ele só funciona no Windows.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Gerenciadores de estado globais (como Provider) são necessários para manter o código organizado quando o app cresce.">Porque torna difícil compartilhar dados entre telas diferentes e pode causar problemas de performance.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciadores de estado globais (como Provider) são necessários para manter o código organizado quando o app cresce.">Porque as cores ficam feias.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual o papel do pacote `Provider`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Provider é um "provedor" de dados que avisa aos widgets quando eles devem se atualizar.">Aumentar a bateria do celular.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Provider é um "provedor" de dados que avisa aos widgets quando eles devem se atualizar.">Facilitar o compartilhamento de dados e o gerenciamento de estado de forma reativa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Provider é um "provedor" de dados que avisa aos widgets quando eles devem se atualizar.">Criar ícones personalizados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Provider é um "provedor" de dados que avisa aos widgets quando eles devem se atualizar.">Traduzir o app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que faz o método `notifyListeners()`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem o `notifyListeners`, os dados mudam no código, mas a tela continua igual.">Toca um som de notificação.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem o `notifyListeners`, os dados mudam no código, mas a tela continua igual.">Avisa a todos os widgets que estão escutando o Provider que os dados mudaram.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem o `notifyListeners`, os dados mudam no código, mas a tela continua igual.">Fecha o aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem o `notifyListeners`, os dados mudam no código, mas a tela continua igual.">Envia um e-mail.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Onde devemos colocar o `ChangeNotifierProvider` para que o app inteiro tenha acesso aos dados?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Colocando no topo da árvore de widgets, todos os ramos abaixo podem "beber" dessa fonte de dados.">No final do arquivo main.dart.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Colocando no topo da árvore de widgets, todos os ramos abaixo podem "beber" dessa fonte de dados.">Envolvendo o widget `MaterialApp` (raiz do projeto).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Colocando no topo da árvore de widgets, todos os ramos abaixo podem "beber" dessa fonte de dados.">Dentro de cada página.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Colocando no topo da árvore de widgets, todos os ramos abaixo podem "beber" dessa fonte de dados.">No `pubspec.yaml`.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual a diferença entre `watch` e `read` no contexto do Provider?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Use `watch` para exibir valores na tela e `read` para disparar ações (funções).">`read` é mais rápido que `watch`.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Use `watch` para exibir valores na tela e `read` para disparar ações (funções).">`watch` reconstrói o widget quando o dado muda; `read` apenas acessa o dado uma vez (ex: em cliques de botão).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Use `watch` para exibir valores na tela e `read` para disparar ações (funções).">`watch` serve para ver vídeos, `read` para textos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Use `watch` para exibir valores na tela e `read` para disparar ações (funções).">Não há diferença.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é um `Consumer` no pacote Provider?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Consumer` ajuda a otimizar a performance, reconstruindo apenas o pedaço de código que realmente precisa.">O usuário final do aplicativo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `Consumer` ajuda a otimizar a performance, reconstruindo apenas o pedaço de código que realmente precisa.">Um widget que reconstrói apenas uma parte específica da interface quando o estado muda.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Consumer` ajuda a otimizar a performance, reconstruindo apenas o pedaço de código que realmente precisa.">Uma ferramenta para comprar moedas no app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Consumer` ajuda a otimizar a performance, reconstruindo apenas o pedaço de código que realmente precisa.">O nome do banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o comportamento de um `StatelessWidget` em relação ao estado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `Stateless` (Sem Estado) serve para interfaces que não variam após serem criadas.">Ele muda de cor sozinho.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `Stateless` (Sem Estado) serve para interfaces que não variam após serem criadas.">Ele é estático e não possui um mecanismo interno para atualizar sua própria UI.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `Stateless` (Sem Estado) serve para interfaces que não variam após serem criadas.">Ele salva dados no banco.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `Stateless` (Sem Estado) serve para interfaces que não variam após serem criadas.">Ele é um widget nulo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Além do Provider, quais são outras formas comuns de gerenciar estado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. BLoC e Riverpod são alternativas poderosas ao Provider para diferentes fluxos de trabalho.">Excel e Word.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! BLoC e Riverpod são alternativas poderosas ao Provider para diferentes fluxos de trabalho.">BLoC, Riverpod e GetX.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. BLoC e Riverpod são alternativas poderosas ao Provider para diferentes fluxos de trabalho.">HTML e CSS.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. BLoC e Riverpod são alternativas poderosas ao Provider para diferentes fluxos de trabalho.">Photoshop e Figma.</div>
  <div class="quiz-feedback"></div>
</div>
