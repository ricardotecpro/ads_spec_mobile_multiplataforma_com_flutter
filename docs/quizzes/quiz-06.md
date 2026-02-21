# Quiz 06 - Componentes Visuais 🖼️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual propriedade do widget `Text` usamos para mudar a cor e o tamanho da fonte?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Toda a estilização de texto é concentrada na classe `TextStyle`.">font:</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Toda a estilização de texto é concentrada na classe `TextStyle`.">theme:</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Toda a estilização de texto é concentrada na classe `TextStyle`.">style: TextStyle(...)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Toda a estilização de texto é concentrada na classe `TextStyle`.">colorSettings:</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Como exibimos uma imagem vinda de uma URL da internet?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `Image.network` é o construtor específico para carregar imagens via protocolo HTTP.">Image.asset(...)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `Image.network` é o construtor específico para carregar imagens via protocolo HTTP.">Image.network(...)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `Image.network` é o construtor específico para carregar imagens via protocolo HTTP.">Image.file(...)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `Image.network` é o construtor específico para carregar imagens via protocolo HTTP.">Image.url(...)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual o widget de botão padrão que possui cor de fundo e sombra no Material 3?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `ElevatedButton` é o botão de destaque principal na hierarquia visual.">TextButton</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `ElevatedButton` é o botão de destaque principal na hierarquia visual.">OutlinedButton</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `ElevatedButton` é o botão de destaque principal na hierarquia visual.">ElevatedButton</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `ElevatedButton` é o botão de destaque principal na hierarquia visual.">FlatButton</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Para que serve o widget `AppBar`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `AppBar` é a barra superior de navegação e título.">Para mostrar propagandas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A `AppBar` é a barra superior de navegação e título.">Para exibir o título da página e ações no topo da tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `AppBar` é a barra superior de navegação e título.">Para salvar dados no celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `AppBar` é a barra superior de navegação e título.">Para mudar o ícone do app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual widget usamos para exibir ícones prontos do sistema?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter já vem com a biblioteca `Material Icons` integrada.">Img()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter já vem com a biblioteca `Material Icons` integrada.">SVG()</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Flutter já vem com a biblioteca `Material Icons` integrada.">Icon(Icons.nome_do_icone)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter já vem com a biblioteca `Material Icons` integrada.">MaterialDesign()</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual parâmetro de um botão define o que acontece quando ele é clicado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, a função de callback de clique é quase sempre chamada de `onPressed`.">onClick:</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No Flutter, a função de callback de clique é quase sempre chamada de `onPressed`.">onPressed:</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, a função de callback de clique é quase sempre chamada de `onPressed`.">tap:</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, a função de callback de clique é quase sempre chamada de `onPressed`.">execute:</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como transformamos qualquer widget em um botão clicável?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `InkWell` adiciona o efeito visual de "toque" (ripple), enquanto `GestureDetector` captura apenas o gesto.">Envolvendo-o em um `Scaffold`.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `InkWell` adiciona o efeito visual de "toque" (ripple), enquanto `GestureDetector` captura apenas o gesto.">Envolvendo-o em um `GestureDetector` ou `InkWell`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `InkWell` adiciona o efeito visual de "toque" (ripple), enquanto `GestureDetector` captura apenas o gesto.">Usando o comando `makeClickable: true`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `InkWell` adiciona o efeito visual de "toque" (ripple), enquanto `GestureDetector` captura apenas o gesto.">Mudando a cor para azul.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o papel do widget `CircleAvatar`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o widget padrão para representar avatares de usuários.">Criar um botão redondo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele é o widget padrão para representar avatares de usuários.">Exibir uma imagem ou texto em formato circular, comum para fotos de perfil.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o widget padrão para representar avatares de usuários.">Desenhar círculos matemáticos na tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele é o widget padrão para representar avatares de usuários.">Criar um relógio.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O que o widget `Divider` faz?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É um componente visual de separação.">Divide o valor de dois números.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É um componente visual de separação.">Desenha uma linha horizontal fina para separar conteúdos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É um componente visual de separação.">Quebra a interface em duas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É um componente visual de separação.">Fecha o aplicativo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como definimos um ícone que fica no final da `AppBar`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `leading` fica no início (esquerda), `title` no meio e `actions` no final (direita).">Usando o parâmetro `leading`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `leading` fica no início (esquerda), `title` no meio e `actions` no final (direita).">Usando o parâmetro `title`.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `leading` fica no início (esquerda), `title` no meio e `actions` no final (direita).">Usando a lista `actions: []`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `leading` fica no início (esquerda), `title` no meio e `actions` no final (direita).">Usando `trailing`.</div>
  <div class="quiz-feedback"></div>
</div>
