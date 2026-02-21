# Quiz 16 - Revisão Final 🎓

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a linguagem de programação base do Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Dart é o motor lógico e de interface de todo projeto Flutter.">Kotlin</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Dart é o motor lógico e de interface de todo projeto Flutter.">Swift</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Dart é o motor lógico e de interface de todo projeto Flutter.">Dart</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Dart é o motor lógico e de interface de todo projeto Flutter.">Rust</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que é um "Widget" para o Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A filosofia do Flutter é fundamentada na composição de widgets.">Uma função matemática.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A filosofia do Flutter é fundamentada na composição de widgets.">Quase tudo o que compõe a interface e o comportamento do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A filosofia do Flutter é fundamentada na composição de widgets.">O nome do motor gráfico.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A filosofia do Flutter é fundamentada na composição de widgets.">Uma animação 3D.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal vantagem do "Hot Reload"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o que torna o desenvolvimento em Flutter um dos mais produtivos do mercado.">Economiza internet.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É o que torna o desenvolvimento em Flutter um dos mais produtivos do mercado.">Ciclo de desenvolvimento ultra-rápido, vendo mudanças no código quase em tempo real.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o que torna o desenvolvimento em Flutter um dos mais produtivos do mercado.">Deixa o app mais leve.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o que torna o desenvolvimento em Flutter um dos mais produtivos do mercado.">Corrige erros gramaticais.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Como lidamos com dados que precisam ser compartilhados entre muitas telas (Estado Global)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciamento de estado global evita a "bagunça" de passar dados manualmente por dezenas de construtores.">Copiando e colando variáveis.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Gerenciamento de estado global evita a "bagunça" de passar dados manualmente por dezenas de construtores.">Usando gerenciadores de estado como Provider, BLoC ou Riverpod.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciamento de estado global evita a "bagunça" de passar dados manualmente por dezenas de construtores.">Guardando tudo no `main.dart`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciamento de estado global evita a "bagunça" de passar dados manualmente por dezenas de construtores.">Não é possível compartilhar dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve o `Scaffold`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o ponto de partida para a maioria das páginas de um app.">Para rodar o app no iOS.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele é o ponto de partida para a maioria das páginas de um app.">Para fornecer o layout visual básico do Material Design (App Bar, Body, FAB).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o ponto de partida para a maioria das páginas de um app.">Para mudar a versão do Dart.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o ponto de partida para a maioria das páginas de um app.">Para apagar o projeto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o papel do arquivo `pubspec.yaml`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem ele, o Flutter não sabe quais bibliotecas ou imagens seu projeto usa.">Guardar o código das telas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem ele, o Flutter não sabe quais bibliotecas ou imagens seu projeto usa.">Centralizar configurações do projeto, assets e dependências de pacotes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem ele, o Flutter não sabe quais bibliotecas ou imagens seu projeto usa.">Definir as cores do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem ele, o Flutter não sabe quais bibliotecas ou imagens seu projeto usa.">Traduzir o app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Diferença fundamental entre Stateless e Stateful?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Use Stateless para componentes fixos e Stateful para interativos.">Stateless é para web, Stateful para mobile.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Use Stateless para componentes fixos e Stateful para interativos.">Stateless não muda após criado; Stateful pode redesenhar sua UI conforme os dados mudam.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Use Stateless para componentes fixos e Stateful para interativos.">Stateful é proibido no Android.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Use Stateless para componentes fixos e Stateful para interativos.">Stateless carrega mais rápido.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que faz a compilação AOT (Ahead-of-Time)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A compilação antecipada é o segredo para a fluidez das animações no Flutter.">Traduz o código para inglês.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A compilação antecipada é o segredo para a fluidez das animações no Flutter.">Transforma o código Dart em código de máquina nativo de alta performance para a publicação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A compilação antecipada é o segredo para a fluidez das animações no Flutter.">Retarda a execução do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A compilação antecipada é o segredo para a fluidez das animações no Flutter.">Envia o código para o servidor.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o comando para instalar as dependências de um projeto existente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sempre execute este comando ao baixar um projeto do GitHub ou adicionar um novo pacote.">flutter install</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sempre execute este comando ao baixar um projeto do GitHub ou adicionar um novo pacote.">flutter pub get</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sempre execute este comando ao baixar um projeto do GitHub ou adicionar um novo pacote.">pub sync</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sempre execute este comando ao baixar um projeto do GitHub ou adicionar um novo pacote.">flutter download</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O Flutter permite rodar o MESMO código em quais plataformas?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter é o framework multiplataforma mais abrangente da atualidade.">Apenas Android e Web.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter é o framework multiplataforma mais abrangente da atualidade.">Apenas Windows e macOS.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Flutter é o framework multiplataforma mais abrangente da atualidade.">Android, iOS, Web, Windows, macOS e Linux.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter é o framework multiplataforma mais abrangente da atualidade.">Apenas no Chrome.</div>
  <div class="quiz-feedback"></div>
</div>
