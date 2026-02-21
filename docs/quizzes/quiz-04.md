# Quiz 04 - Widgets Básicos 🧱

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é um Widget no Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, absolutamente tudo (botões, textos, alinhamentos) é um Widget.">Uma linha de código JavaScript.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No Flutter, absolutamente tudo (botões, textos, alinhamentos) é um Widget.">A unidade básica de construção da interface do usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, absolutamente tudo (botões, textos, alinhamentos) é um Widget.">Um tipo de banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, absolutamente tudo (botões, textos, alinhamentos) é um Widget.">O ícone do aplicativo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a principal diferença entre StatelessWidget e StatefulWidget?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `StatefulWidget` possui um objeto de estado que permite que a UI seja atualizada dinamicamente.">StatelessWidget é mais rápido.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `StatefulWidget` possui um objeto de estado que permite que a UI seja atualizada dinamicamente.">StatefulWidget não pode ter filhos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `StatefulWidget` possui um objeto de estado que permite que a UI seja atualizada dinamicamente.">StatelessWidget é imutável, enquanto StatefulWidget pode mudar de estado durante a execução.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `StatefulWidget` possui um objeto de estado que permite que a UI seja atualizada dinamicamente.">StatelessWidget só funciona no Android.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual método é obrigatório em todo StatelessWidget?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `build` é onde definimos como o widget deve ser desenhado na tela.">create()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `build` é onde definimos como o widget deve ser desenhado na tela.">initState()</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O método `build` é onde definimos como o widget deve ser desenhado na tela.">build()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `build` é onde definimos como o widget deve ser desenhado na tela.">run()</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Como o Flutter organiza os widgets na tela?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A hierarquia de widgets (pai e filho) forma a Árvore de Widgets.">Em uma lista linear.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A hierarquia de widgets (pai e filho) forma a Árvore de Widgets.">Em uma tabela de pixels.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A hierarquia de widgets (pai e filho) forma a Árvore de Widgets.">Em uma estrutura de árvore (Widget Tree).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A hierarquia de widgets (pai e filho) forma a Árvore de Widgets.">De forma aleatória.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve o widget `Scaffold`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Scaffold` é o "esqueleto" que implementa o layout visual básico do Material Design.">Para criar animações complexas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `Scaffold` é o "esqueleto" que implementa o layout visual básico do Material Design.">Para fornecer uma estrutura visual básica (AppBar, Body, FloatingActionButton).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Scaffold` é o "esqueleto" que implementa o layout visual básico do Material Design.">Para conectar ao banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Scaffold` é o "esqueleto" que implementa o layout visual básico do Material Design.">Para mudar a cor do texto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual widget usamos para centralizar um filho na tela?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O widget `Center` alinha seu filho exatamente no meio do espaço disponível.">Middle</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O widget `Center` alinha seu filho exatamente no meio do espaço disponível.">Center</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O widget `Center` alinha seu filho exatamente no meio do espaço disponível.">AlignMiddle</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O widget `Center` alinha seu filho exatamente no meio do espaço disponível.">Column</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que acontece quando chamamos `setState()`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `setState` notifica o framework de que o estado interno mudou, disparando o método `build` novamente.">O app fecha.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `setState` notifica o framework de que o estado interno mudou, disparando o método `build` novamente.">O banco de dados é limpo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `setState` notifica o framework de que o estado interno mudou, disparando o método `build` novamente.">O Flutter marca o widget para ser reconstruído com os novos dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `setState` notifica o framework de que o estado interno mudou, disparando o método `build` novamente.">O código Dart é deletado.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o papel do `MaterialApp`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o widget raiz que envolve todo o sistema de design Material do app.">Definir o nome do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele é o widget raiz que envolve todo o sistema de design Material do app.">Configurar o tema global, rotas e idioma do aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o widget raiz que envolve todo o sistema de design Material do app.">Criar um banco de dados SQL.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o widget raiz que envolve todo o sistema de design Material do app.">Aumentar a velocidade da internet.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Widgets no Flutter são inspirados em qual outro framework famoso?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter utiliza uma abordagem declarativa de UI, similar ao React.">Angular</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Flutter utiliza uma abordagem declarativa de UI, similar ao React.">React (pela abordagem declarativa)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter utiliza uma abordagem declarativa de UI, similar ao React.">Vue</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter utiliza uma abordagem declarativa de UI, similar ao React.">Django</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como adicionamos um comentário em uma única linha no código Dart de um Widget?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Assim como em Java/C/JS, o Dart usa `//` para comentários de linha."># comentário</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Assim como em Java/C/JS, o Dart usa `//` para comentários de linha."><!-- comentário --></div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Assim como em Java/C/JS, o Dart usa `//` para comentários de linha.">// comentário</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Assim como em Java/C/JS, o Dart usa `//` para comentários de linha.">/* comentário */</div>
  <div class="quiz-feedback"></div>
</div>
