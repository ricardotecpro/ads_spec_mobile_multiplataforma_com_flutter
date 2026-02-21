# Quiz 08 - Formulários e Validação 📝

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual widget é a entrada de texto mais básica do Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `TextField` é o componente padrão para capturar inputs do teclado.">TextArea</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `TextField` é o componente padrão para capturar inputs do teclado.">InputBox</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `TextField` é o componente padrão para capturar inputs do teclado.">TextField</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `TextField` é o componente padrão para capturar inputs do teclado.">TextForm</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para que serve o `TextEditingController`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O controlador permite ler o valor do campo e também preenchê-lo programaticamente.">Para mudar a cor do teclado.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O controlador permite ler o valor do campo e também preenchê-lo programaticamente.">Para controlar e capturar o texto digitado pelo usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O controlador permite ler o valor do campo e também preenchê-lo programaticamente.">Para apagar o histórico do navegador.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O controlador permite ler o valor do campo e também preenchê-lo programaticamente.">Para formatar números.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal vantagem do `TextFormField` sobre o `TextField`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `TextFormField` simplifica o processo de validar regras (como "campo obrigatório").">É mais bonito.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `TextFormField` simplifica o processo de validar regras (como "campo obrigatório").">Possui integração nativa com o widget `Form` para validação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `TextFormField` simplifica o processo de validar regras (como "campo obrigatório").">Aceita apenas números.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `TextFormField` simplifica o processo de validar regras (como "campo obrigatório").">Não precisa de controlador.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Como acionamos a validação de todos os campos de um formulário?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `GlobalKey` permite acessar o estado interno do formulário de qualquer lugar.">Clicando em qualquer lugar da tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `GlobalKey` permite acessar o estado interno do formulário de qualquer lugar.">Chamando o método `validateAll()`.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A `GlobalKey` permite acessar o estado interno do formulário de qualquer lugar.">Usando uma chave global (`GlobalKey<FormState>`) e chamando `_formKey.currentState!.validate()`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `GlobalKey` permite acessar o estado interno do formulário de qualquer lugar.">O Flutter valida automaticamente em tempo real.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que a função `validator` deve retornar se a entrada do usuário for válida?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, retornar `null` indica que não há erro; qualquer String retornada é exibida como mensagem de erro.">"Ok"</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, retornar `null` indica que não há erro; qualquer String retornada é exibida como mensagem de erro.">true</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No Flutter, retornar `null` indica que não há erro; qualquer String retornada é exibida como mensagem de erro.">null</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Flutter, retornar `null` indica que não há erro; qualquer String retornada é exibida como mensagem de erro.">uma String vazia ""</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual propriedade do `TextField` usamos para ocultar a senha (exibir asteriscos)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `obscureText` é o padrão para campos de senha.">passwordMode: true</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `obscureText` é o padrão para campos de senha.">hideText: true</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `obscureText` é o padrão para campos de senha.">obscureText: true</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `obscureText` é o padrão para campos de senha.">secret: true</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como mudamos o tipo de teclado (ex: teclado numérico ou de e-mail)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `TextInputType` permite otimizar a experiência do usuário dependendo do dado esperado.">Através da propriedade `keyboardType: TextInputType.number`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `TextInputType` permite otimizar a experiência do usuário dependendo do dado esperado.">O Flutter detecta automaticamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `TextInputType` permite otimizar a experiência do usuário dependendo do dado esperado.">Não é possível mudar o teclado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `TextInputType` permite otimizar a experiência do usuário dependendo do dado esperado.">Mudando a fonte do texto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Para que serve a propriedade `decoration` no TextField?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `InputDecoration` cuida de toda a perfumaria e rótulos do campo.">Para adicionar bordas, ícones, labels e dicas (placeholders).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `InputDecoration` cuida de toda a perfumaria e rótulos do campo.">Para mudar a linguagem do teclado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `InputDecoration` cuida de toda a perfumaria e rótulos do campo.">Para rodar o app mais rápido.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `InputDecoration` cuida de toda a perfumaria e rótulos do campo.">Para deletar o texto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Onde devemos instanciar o `TextEditingController` em um StatefulWidget?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Instanciar dentro do `build` faria o controlador ser reiniciado a cada redesenho da tela, perdendo o dado.">Dentro do método build.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Instanciar dentro do `build` faria o controlador ser reiniciado a cada redesenho da tela, perdendo o dado.">No `initState` ou diretamente na classe (fora do build).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Instanciar dentro do `build` faria o controlador ser reiniciado a cada redesenho da tela, perdendo o dado.">No `pubspec.yaml`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Instanciar dentro do `build` faria o controlador ser reiniciado a cada redesenho da tela, perdendo o dado.">No `main.dart`.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual widget usamos para mostrar uma mensagem rápida na parte inferior da tela após submeter um formulário?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `SnackBar` é o padrão do Material Design para feedbacks rápidos e temporários.">AlertBox</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A `SnackBar` é o padrão do Material Design para feedbacks rápidos e temporários.">SnackBar</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `SnackBar` é o padrão do Material Design para feedbacks rápidos e temporários.">Toast</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `SnackBar` é o padrão do Material Design para feedbacks rápidos e temporários.">BottomSheet</div>
  <div class="quiz-feedback"></div>
</div>
