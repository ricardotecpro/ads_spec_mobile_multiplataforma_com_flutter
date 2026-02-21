# Quiz 09 - Gerenciamento de Estado 🔄

1. O que é "Estado" no Flutter?
    - [ ] O país onde o desenvolvedor mora.
    - [x] Dados que podem mudar e que afetam o que é exibido na tela.
    - [ ] O tamanho do arquivo do aplicativo.
    - [ ] O ícone da bateria do celular.
    *Explicação: Estado é a "memória" do app: um contador, se um botão está ativo, ou dados de um usuário logado.*

2. Qual o comando básico para atualizar a tela em um StatefulWidget?
    - [ ] refresh()
    - [ ] updateUI()
    - [x] setState()
    - [ ] reload()
    *Explicação: O `setState` avisa ao Flutter que os dados mudaram e que o método `build` precisa rodar de novo.*

3. Por que o `setState()` não é recomendado para aplicativos grandes e complexos?
    - [ ] Porque ele apaga o banco de dados.
    - [ ] Porque ele só funciona no Windows.
    - [x] Porque torna difícil compartilhar dados entre telas diferentes e pode causar problemas de performance.
    - [ ] Porque as cores ficam feias.
    *Explicação: Gerenciadores de estado globais (como Provider) são necessários para manter o código organizado quando o app cresce.*

4. Qual o papel do pacote `Provider`?
    - [ ] Aumentar a bateria do celular.
    - [x] Facilitar o compartilhamento de dados e o gerenciamento de estado de forma reativa.
    - [ ] Criar ícones personalizados.
    - [ ] Traduzir o app.
    *Explicação: O Provider é um "provedor" de dados que avisa aos widgets quando eles devem se atualizar.*

5. O que faz o método `notifyListeners()`?
    - [ ] Toca um som de notificação.
    - [x] Avisa a todos os widgets que estão escutando o Provider que os dados mudaram.
    - [ ] Fecha o aplicativo.
    - [ ] Envia um e-mail.
    *Explicação: Sem o `notifyListeners`, os dados mudam no código, mas a tela continua igual.*

6. Onde devemos colocar o `ChangeNotifierProvider` para que o app inteiro tenha acesso aos dados?
    - [ ] No final do arquivo main.dart.
    - [x] Envolvendo o widget `MaterialApp` (raiz do projeto).
    - [ ] Dentro de cada página.
    - [ ] No `pubspec.yaml`.
    *Explicação: Colocando no topo da árvore de widgets, todos os ramos abaixo podem "beber" dessa fonte de dados.*

7. Qual a diferença entre `watch` e `read` no contexto do Provider?
    - [ ] `read` é mais rápido que `watch`.
    - [x] `watch` reconstrói o widget quando o dado muda; `read` apenas acessa o dado uma vez (ex: em cliques de botão).
    - [ ] `watch` serve para ver vídeos, `read` para textos.
    - [ ] Não há diferença.
    *Explicação: Use `watch` para exibir valores na tela e `read` para disparar ações (funções).*

8. O que é um `Consumer` no pacote Provider?
    - [ ] O usuário final do aplicativo.
    - [x] Um widget que reconstrói apenas uma parte específica da interface quando o estado muda.
    - [ ] Uma ferramenta para comprar moedas no app.
    - [ ] O nome do banco de dados.
    *Explicação: O `Consumer` ajuda a otimizar a performance, reconstruindo apenas o pedaço de código que realmente precisa.*

9. Qual o comportamento de um `StatelessWidget` em relação ao estado?
    - [ ] Ele muda de cor sozinho.
    - [x] Ele é estático e não possui um mecanismo interno para atualizar sua própria UI.
    - [ ] Ele salva dados no banco.
    - [ ] Ele é um widget nulo.
    *Explicação: `Stateless` (Sem Estado) serve para interfaces que não variam após serem criadas.*

10. Além do Provider, quais são outras formas comuns de gerenciar estado?
    - [ ] Excel e Word.
    - [x] BLoC, Riverpod e GetX.
    - [ ] HTML e CSS.
    - [ ] Photoshop e Figma.
    *Explicação: BLoC e Riverpod são alternativas poderosas ao Provider para diferentes fluxos de trabalho.*