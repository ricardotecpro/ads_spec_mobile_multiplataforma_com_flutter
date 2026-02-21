# Quiz 02 - Linguagem Dart para Iniciantes 🎯

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é o Dart?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Dart é a linguagem base do Flutter, focada em performance e UI.">Um framework para CSS.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Dart é a linguagem base do Flutter, focada em performance e UI.">Uma linguagem de programação de tipagem forte criada pelo Google.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Dart é a linguagem base do Flutter, focada em performance e UI.">O nome do motor gráfico do Flutter.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Dart é a linguagem base do Flutter, focada em performance e UI.">Uma ferramenta de design para prototipagem.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Como declaramos uma variável com inferência de tipo no Dart?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `var` permite que o Dart descubra o tipo da variável automaticamente pelo valor atribuído.">int x = 10;</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `var` permite que o Dart descubra o tipo da variável automaticamente pelo valor atribuído.">string nome = "Oi";</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `var` permite que o Dart descubra o tipo da variável automaticamente pelo valor atribuído.">var valor = 50;</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `var` permite que o Dart descubra o tipo da variável automaticamente pelo valor atribuído.">dynamic x = 10;</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que é o "Null Safety" no Dart?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Null Safety obriga o programador a tratar valores nulos explicitamente, evitando o famoso "null pointer exception".">Uma forma de apagar todas as variáveis nulas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Null Safety obriga o programador a tratar valores nulos explicitamente, evitando o famoso "null pointer exception".">Um recurso que evita erros de acesso a referências nulas em tempo de compilação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Null Safety obriga o programador a tratar valores nulos explicitamente, evitando o famoso "null pointer exception".">Um sistema de segurança contra vírus.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Null Safety obriga o programador a tratar valores nulos explicitamente, evitando o famoso "null pointer exception".">Um modo de converter nulos em zeros.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual operador usamos para permitir que uma variável aceite valores nulos?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `?` após o tipo (ex: `String?`) indica que aquela variável pode receber `null`.">!</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `?` após o tipo (ex: `String?`) indica que aquela variável pode receber `null`.">?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `?` após o tipo (ex: `String?`) indica que aquela variável pode receber `null`.">??</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `?` após o tipo (ex: `String?`) indica que aquela variável pode receber `null`.">.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Como se define uma função que não retorna nenhum valor?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `void` é a palavra-chave para funções que executam uma tarefa sem devolver um resultado.">def</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `void` é a palavra-chave para funções que executam uma tarefa sem devolver um resultado.">function</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `void` é a palavra-chave para funções que executam uma tarefa sem devolver um resultado.">empty</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `void` é a palavra-chave para funções que executam uma tarefa sem devolver um resultado.">void</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual a saída do código: `var x = "10"; print(x.runtimeType);`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como o valor está entre aspas, o Dart infere que o tipo é String.">int</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Como o valor está entre aspas, o Dart infere que o tipo é String.">String</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como o valor está entre aspas, o Dart infere que o tipo é String.">dynamic</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como o valor está entre aspas, o Dart infere que o tipo é String.">double</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Para que serve o operador `??` no Dart?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ex: `nome ?? "Anônimo"` retorna "Anônimo" se `nome` for nulo.">Comparar se dois valores são nulos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ex: `nome ?? "Anônimo"` retorna "Anônimo" se `nome` for nulo.">Fornecer um valor padrão caso o operando da esquerda seja nulo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ex: `nome ?? "Anônimo"` retorna "Anônimo" se `nome` for nulo.">Forçar uma variável a ser nula.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ex: `nome ?? "Anônimo"` retorna "Anônimo" se `nome` for nulo.">Multiplicar dois valores.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o tipo de dado correto para números decimais (ex: 3.14)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Dart, números de ponto flutuante são do tipo `double`.">int</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Dart, números de ponto flutuante são do tipo `double`.">float</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No Dart, números de ponto flutuante são do tipo `double`.">double</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Dart, números de ponto flutuante são do tipo `double`.">decimal</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O que faz o comando `final` antes de uma variável?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `final` define uma constante que só pode ser definida uma única vez.">Torna a variável global.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `final` define uma constante que só pode ser definida uma única vez.">Impede que o valor da variável seja alterado após a primeira atribuição.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `final` define uma constante que só pode ser definida uma única vez.">Deleta a variável após o uso.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `final` define uma constante que só pode ser definida uma única vez.">Faz a variável ser nula.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como realizamos a interpolação de strings no Dart?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O símbolo `$` permite inserir o valor de uma variável diretamente dentro de uma String.">"Olá " + nome</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O símbolo `$` permite inserir o valor de uma variável diretamente dentro de uma String.">"Olá $nome"</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O símbolo `$` permite inserir o valor de uma variável diretamente dentro de uma String.">"Olá {nome}"</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O símbolo `$` permite inserir o valor de uma variável diretamente dentro de uma String.">"Olá #nome"</div>
  <div class="quiz-feedback"></div>
</div>
