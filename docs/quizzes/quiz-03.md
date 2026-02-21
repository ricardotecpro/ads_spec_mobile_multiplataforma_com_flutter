# Quiz 03 - Estrutura de um Projeto Flutter 🏗️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a pasta onde a maior parte do código fonte (.dart) deve ficar?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A pasta `lib` é o diretório principal para o desenvolvimento do código da aplicação.">assets/</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A pasta `lib` é o diretório principal para o desenvolvimento do código da aplicação.">android/</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A pasta `lib` é o diretório principal para o desenvolvimento do código da aplicação.">lib/</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A pasta `lib` é o diretório principal para o desenvolvimento do código da aplicação.">test/</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para que serve o arquivo `pubspec.yaml`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o manifesto do projeto, onde listamos pacotes externos e configurações globais.">Gerenciar as imagens do Android.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele é o manifesto do projeto, onde listamos pacotes externos e configurações globais.">Configurar metadados, versões e dependências do projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o manifesto do projeto, onde listamos pacotes externos e configurações globais.">Guardar as senhas do banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o manifesto do projeto, onde listamos pacotes externos e configurações globais.">Definir o design das telas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual comando baixamos as dependências listadas no `pubspec.yaml`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `pub get` sincroniza as dependências declaradas com o seu ambiente local.">flutter install</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `pub get` sincroniza as dependências declaradas com o seu ambiente local.">flutter pub get</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `pub get` sincroniza as dependências declaradas com o seu ambiente local.">flutter update</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `pub get` sincroniza as dependências declaradas com o seu ambiente local.">pub download</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Onde configuramos as imagens (assets) do nosso aplicativo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Todos os recursos externos como imagens e fontes precisam ser registrados no `pubspec.yaml`.">No arquivo main.dart.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Todos os recursos externos como imagens e fontes precisam ser registrados no `pubspec.yaml`.">Na pasta android/app/src.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Todos os recursos externos como imagens e fontes precisam ser registrados no `pubspec.yaml`.">Na seção `flutter: assets:` do pubspec.yaml.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Todos os recursos externos como imagens e fontes precisam ser registrados no `pubspec.yaml`.">Não é necessário configurar.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a função da pasta `test/`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É a pasta dedicada à garantia de qualidade através de testes automáticos.">Guardar códigos que não funcionam.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É a pasta dedicada à garantia de qualidade através de testes automáticos.">Armazenar testes automatizados de unidade, widget e integração.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É a pasta dedicada à garantia de qualidade através de testes automáticos.">Reservada para o Google.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É a pasta dedicada à garantia de qualidade através de testes automáticos.">Guardar versões antigas do app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o ponto de entrada (entry point) de um aplicativo Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Todo programa Dart começa sua execução pela função global `main()`.">A class MyApp.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Todo programa Dart começa sua execução pela função global `main()`.">A função main().</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Todo programa Dart começa sua execução pela função global `main()`.">O arquivo pubspec.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Todo programa Dart começa sua execução pela função global `main()`.">O Gradle.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que contém as pastas `android/`, `ios/` e `web/`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Elas contêm os "wrappers" nativos que permitem ao Flutter interagir com o sistema operacional.">Backups do código Dart.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Elas contêm os "wrappers" nativos que permitem ao Flutter interagir com o sistema operacional.">Código nativo necessário para hospedar e rodar o app em cada plataforma.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Elas contêm os "wrappers" nativos que permitem ao Flutter interagir com o sistema operacional.">Tutoriais de cada sistema.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Elas contêm os "wrappers" nativos que permitem ao Flutter interagir com o sistema operacional.">Fotos do projeto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. No `pubspec.yaml`, o que indica o `^` antes da versão de um pacote?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O circunflexo indica compatibilidade semântica para atualizações seguras.">Que a versão é opcional.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O circunflexo indica compatibilidade semântica para atualizações seguras.">Que o Flutter pode baixar versões compatíveis mais recentes (patches/minors).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O circunflexo indica compatibilidade semântica para atualizações seguras.">Que a versão deve ser exatamente aquela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O circunflexo indica compatibilidade semântica para atualizações seguras.">Que o pacote é do Google.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual widget é quase sempre o primeiro a ser chamado dentro do `runApp()`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialApp` configura o sistema de design, navegação e temas para todo o app.">Scaffold</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `MaterialApp` configura o sistema de design, navegação e temas para todo o app.">MaterialApp</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialApp` configura o sistema de design, navegação e temas para todo o app.">Center</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `MaterialApp` configura o sistema de design, navegação e temas para todo o app.">Text</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que é o `.metadata` em um projeto Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É um arquivo de controle interno do Flutter SDK que não deve ser editado manualmente.">Suas fotos pessoais.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É um arquivo de controle interno do Flutter SDK que não deve ser editado manualmente.">Um arquivo gerado automaticamente para rastrear propriedades do projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É um arquivo de controle interno do Flutter SDK que não deve ser editado manualmente.">Onde se escreve o código do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É um arquivo de controle interno do Flutter SDK que não deve ser editado manualmente.">Um vírus.</div>
  <div class="quiz-feedback"></div>
</div>
