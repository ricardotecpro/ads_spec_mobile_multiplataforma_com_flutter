# Quiz 07 - Navegação entre Telas 🛣️

1. Qual classe é responsável por gerenciar a pilha de telas no Flutter?
    - [ ] ScreenManager
    - [x] Navigator
    - [ ] Router
    - [ ] StackController
    *Explicação: O `Navigator` controla a transição e a memória das telas visitadas.*

2. O que o comando `Navigator.push()` faz?
    - [ ] Deleta a tela atual.
    - [x] Adiciona uma nova tela ao topo da pilha de navegação.
    - [ ] Reinicia o aplicativo.
    - [ ] Fecha o aplicativo.
    *Explicação: Puxar (push) uma tela significa colocá-la na frente do usuário.*

3. Como voltamos para a tela anterior programaticamente?
    - [ ] Navigator.back(context)
    - [x] Navigator.pop(context)
    - [ ] Navigator.remove(context)
    - [ ] context.goBack()
    *Explicação: O comando `pop` retira o prato (tela) do topo da pilha, revelando o que estava embaixo.*

4. O que é uma "Rota Nomeada"?
    - [ ] Uma foto da tela.
    - [x] Uma String que identifica uma tela de forma única (ex: '/login').
    - [ ] O nome do autor do código.
    - [ ] Um tipo de botão.
    *Explicação: Rotas nomeadas facilitam a organização em aplicativos que possuem muitas telas.*

5. Onde definimos o mapa de rotas nomeadas de um aplicativo?
    - [ ] No Scaffold.
    - [x] No MaterialApp (parâmetro routes).
    - [ ] No arquivo pubspec.yaml.
    - [ ] Dentro do método build de cada tela.
    *Explicação: O `MaterialApp` centraliza a configuração de navegação do projeto.*

6. Qual widget é usado para criar a transição visual padrão entre telas no Android e iOS?
    - [ ] BoxRoute
    - [ ] CustomRoute
    - [x] MaterialPageRoute
    - [ ] AppRoute
    *Explicação: O `MaterialPageRoute` adapta a animação de entrada conforme o sistema operacional (subida no iOS, fade no Android).*

7. Como passamos dados de uma tela para outra de forma simples?
    - [ ] Salvando em um arquivo de texto.
    - [x] Através do construtor da classe da nova tela.
    - [ ] Usando o comando `sendData()`.
    - [ ] Não é possível passar dados.
    *Explicação: Passar argumentos via construtor é a forma mais direta e segura de transferir informações.*

8. O que acontece se chamarmos `Navigator.pop()` na única tela do app?
    - [ ] O app mostra um erro fatal.
    - [ ] Nada acontece.
    - [x] O aplicativo geralmente é encerrado (fechado).
    - [ ] O app volta para a tela de boot.
    *Explicação: Sem nada abaixo na pilha, o pop retira a última instância e encerra o processo visual.*

9. Qual a diferença entre `push` e `pushReplacement`?
    - [ ] Nenhuma, são sinônimos.
    - [ ] `pushReplacement` é mais lento.
    - [x] `pushReplacement` substitui a tela atual na pilha em vez de apenas empilhar por cima.
    - [ ] `pushReplacement` apaga o banco de dados.
    *Explicação: Útil para telas de Login ou Splash Screens onde você não quer que o usuário volte ao clicar em "Voltar".*

10. Como definimos qual tela será a primeira a abrir no app usando rotas?
    - [ ] Parâmetro `start:`.
    - [ ] Parâmetro `home:`.
    - [x] Parâmetro `initialRoute:`.
    - [ ] Parâmetro `first:`.
    *Explicação: `initialRoute` define o ponto de partida do fluxo de navegação.*