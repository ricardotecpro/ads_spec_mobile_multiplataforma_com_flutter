# Quiz 03 - Estrutura de um Projeto Flutter 🏗️

1. Qual a pasta onde a maior parte do código fonte (.dart) deve ficar?
    - [ ] assets/
    - [ ] android/
    - [x] lib/
    - [ ] test/
    *Explicação: A pasta `lib` é o diretório principal para o desenvolvimento do código da aplicação.*

2. Para que serve o arquivo `pubspec.yaml`?
    - [ ] Gerenciar as imagens do Android.
    - [x] Configurar metadados, versões e dependências do projeto.
    - [ ] Guardar as senhas do banco de dados.
    - [ ] Definir o design das telas.
    *Explicação: Ele é o manifesto do projeto, onde listamos pacotes externos e configurações globais.*

3. Qual comando baixamos as dependências listadas no `pubspec.yaml`?
    - [ ] flutter install
    - [x] flutter pub get
    - [ ] flutter update
    - [ ] pub download
    *Explicação: O `pub get` sincroniza as dependências declaradas com o seu ambiente local.*

4. Onde configuramos as imagens (assets) do nosso aplicativo?
    - [ ] No arquivo main.dart.
    - [ ] Na pasta android/app/src.
    - [x] Na seção `flutter: assets:` do pubspec.yaml.
    - [ ] Não é necessário configurar.
    *Explicação: Todos os recursos externos como imagens e fontes precisam ser registrados no `pubspec.yaml`.*

5. Qual a função da pasta `test/`?
    - [ ] Guardar códigos que não funcionam.
    - [x] Armazenar testes automatizados de unidade, widget e integração.
    - [ ] Reservada para o Google.
    - [ ] Guardar versões antigas do app.
    *Explicação: É a pasta dedicada à garantia de qualidade através de testes automáticos.*

6. Qual o ponto de entrada (entry point) de um aplicativo Flutter?
    - [ ] A class MyApp.
    - [x] A função main().
    - [ ] O arquivo pubspec.
    - [ ] O Gradle.
    *Explicação: Todo programa Dart começa sua execução pela função global `main()`.*

7. O que contém as pastas `android/`, `ios/` e `web/`?
    - [ ] Backups do código Dart.
    - [x] Código nativo necessário para hospedar e rodar o app em cada plataforma.
    - [ ] Tutoriais de cada sistema.
    - [ ] Fotos do projeto.
    *Explicação: Elas contêm os "wrappers" nativos que permitem ao Flutter interagir com o sistema operacional.*

8. No `pubspec.yaml`, o que indica o `^` antes da versão de um pacote?
    - [ ] Que a versão é opcional.
    - [x] Que o Flutter pode baixar versões compatíveis mais recentes (patches/minors).
    - [ ] Que a versão deve ser exatamente aquela.
    - [ ] Que o pacote é do Google.
    *Explicação: O circunflexo indica compatibilidade semântica para atualizações seguras.*

9. Qual widget é quase sempre o primeiro a ser chamado dentro do `runApp()`?
    - [ ] Scaffold
    - [x] MaterialApp
    - [ ] Center
    - [ ] Text
    *Explicação: O `MaterialApp` configura o sistema de design, navegação e temas para todo o app.*

10. O que é o `.metadata` em um projeto Flutter?
    - [ ] Suas fotos pessoais.
    - [x] Um arquivo gerado automaticamente para rastrear propriedades do projeto.
    - [ ] Onde se escreve o código do app.
    - [ ] Um vírus.
    *Explicação: É um arquivo de controle interno do Flutter SDK que não deve ser editado manualmente.*
