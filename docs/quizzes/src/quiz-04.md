# Quiz 04 - Widgets Básicos 🧱

1. O que é um Widget no Flutter?
    - [ ] Uma linha de código JavaScript.
    - [x] A unidade básica de construção da interface do usuário.
    - [ ] Um tipo de banco de dados.
    - [ ] O ícone do aplicativo.
    *Explicação: No Flutter, absolutamente tudo (botões, textos, alinhamentos) é um Widget.*

2. Qual a principal diferença entre StatelessWidget e StatefulWidget?
    - [ ] StatelessWidget é mais rápido.
    - [ ] StatefulWidget não pode ter filhos.
    - [x] StatelessWidget é imutável, enquanto StatefulWidget pode mudar de estado durante a execução.
    - [ ] StatelessWidget só funciona no Android.
    *Explicação: O `StatefulWidget` possui um objeto de estado que permite que a UI seja atualizada dinamicamente.*

3. Qual método é obrigatório em todo StatelessWidget?
    - [ ] create()
    - [ ] initState()
    - [x] build()
    - [ ] run()
    *Explicação: O método `build` é onde definimos como o widget deve ser desenhado na tela.*

4. Como o Flutter organiza os widgets na tela?
    - [ ] Em uma lista linear.
    - [ ] Em uma tabela de pixels.
    - [x] Em uma estrutura de árvore (Widget Tree).
    - [ ] De forma aleatória.
    *Explicação: A hierarquia de widgets (pai e filho) forma a Árvore de Widgets.*

5. Para que serve o widget `Scaffold`?
    - [ ] Para criar animações complexas.
    - [x] Para fornecer uma estrutura visual básica (AppBar, Body, FloatingActionButton).
    - [ ] Para conectar ao banco de dados.
    - [ ] Para mudar a cor do texto.
    *Explicação: O `Scaffold` é o "esqueleto" que implementa o layout visual básico do Material Design.*

6. Qual widget usamos para centralizar um filho na tela?
    - [ ] Middle
    - [x] Center
    - [ ] AlignMiddle
    - [ ] Column
    *Explicação: O widget `Center` alinha seu filho exatamente no meio do espaço disponível.*

7. O que acontece quando chamamos `setState()`?
    - [ ] O app fecha.
    - [ ] O banco de dados é limpo.
    - [x] O Flutter marca o widget para ser reconstruído com os novos dados.
    - [ ] O código Dart é deletado.
    *Explicação: O `setState` notifica o framework de que o estado interno mudou, disparando o método `build` novamente.*

8. Qual o papel do `MaterialApp`?
    - [ ] Definir o nome do desenvolvedor.
    - [x] Configurar o tema global, rotas e idioma do aplicativo.
    - [ ] Criar um banco de dados SQL.
    - [ ] Aumentar a velocidade da internet.
    *Explicação: Ele é o widget raiz que envolve todo o sistema de design Material do app.*

9. Widgets no Flutter são inspirados em qual outro framework famoso?
    - [ ] Angular
    - [x] React (pela abordagem declarativa)
    - [ ] Vue
    - [ ] Django
    *Explicação: O Flutter utiliza uma abordagem declarativa de UI, similar ao React.*

10. Como adicionamos um comentário em uma única linha no código Dart de um Widget?
    - [ ] # comentário
    - [ ] <!-- comentário -->
    - [x] // comentário
    - [ ] /* comentário */
    *Explicação: Assim como em Java/C/JS, o Dart usa `//` para comentários de linha.*
