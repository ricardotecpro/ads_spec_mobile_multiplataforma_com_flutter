# Quiz 08 - Formulários e Validação 📝

1. Qual widget é a entrada de texto mais básica do Flutter?
    - [ ] TextArea
    - [ ] InputBox
    - [x] TextField
    - [ ] TextForm
    *Explicação: O `TextField` é o componente padrão para capturar inputs do teclado.*

2. Para que serve o `TextEditingController`?
    - [ ] Para mudar a cor do teclado.
    - [x] Para controlar e capturar o texto digitado pelo usuário.
    - [ ] Para apagar o histórico do navegador.
    - [ ] Para formatar números.
    *Explicação: O controlador permite ler o valor do campo e também preenchê-lo programaticamente.*

3. Qual a principal vantagem do `TextFormField` sobre o `TextField`?
    - [ ] É mais bonito.
    - [x] Possui integração nativa com o widget `Form` para validação.
    - [ ] Aceita apenas números.
    - [ ] Não precisa de controlador.
    *Explicação: O `TextFormField` simplifica o processo de validar regras (como "campo obrigatório").*

4. Como acionamos a validação de todos os campos de um formulário?
    - [ ] Clicando em qualquer lugar da tela.
    - [ ] Chamando o método `validateAll()`.
    - [x] Usando uma chave global (`GlobalKey<FormState>`) e chamando `_formKey.currentState!.validate()`.
    - [ ] O Flutter valida automaticamente em tempo real.
    *Explicação: A `GlobalKey` permite acessar o estado interno do formulário de qualquer lugar.*

5. O que a função `validator` deve retornar se a entrada do usuário for válida?
    - [ ] "Ok"
    - [ ] true
    - [x] null
    - [ ] uma String vazia ""
    *Explicação: No Flutter, retornar `null` indica que não há erro; qualquer String retornada é exibida como mensagem de erro.*

6. Qual propriedade do `TextField` usamos para ocultar a senha (exibir asteriscos)?
    - [ ] passwordMode: true
    - [ ] hideText: true
    - [x] obscureText: true
    - [ ] secret: true
    *Explicação: `obscureText` é o padrão para campos de senha.*

7. Como mudamos o tipo de teclado (ex: teclado numérico ou de e-mail)?
    - [ ] Através da propriedade `keyboardType: TextInputType.number`.
    - [ ] O Flutter detecta automaticamente.
    - [ ] Não é possível mudar o teclado.
    - [ ] Mudando a fonte do texto.
    *Explicação: `TextInputType` permite otimizar a experiência do usuário dependendo do dado esperado.*

8. Para que serve a propriedade `decoration` no TextField?
    - [ ] Para adicionar bordas, ícones, labels e dicas (placeholders).
    - [ ] Para mudar a linguagem do teclado.
    - [ ] Para rodar o app mais rápido.
    - [ ] Para deletar o texto.
    *Explicação: O `InputDecoration` cuida de toda a perfumaria e rótulos do campo.*

9. Onde devemos instanciar o `TextEditingController` em um StatefulWidget?
    - [ ] Dentro do método build.
    - [x] No `initState` ou diretamente na classe (fora do build).
    - [ ] No `pubspec.yaml`.
    - [ ] No `main.dart`.
    *Explicação: Instanciar dentro do `build` faria o controlador ser reiniciado a cada redesenho da tela, perdendo o dado.*

10. Qual widget usamos para mostrar uma mensagem rápida na parte inferior da tela após submeter um formulário?
    - [ ] AlertBox
    - [x] SnackBar
    - [ ] Toast
    - [ ] BottomSheet
    *Explicação: A `SnackBar` é o padrão do Material Design para feedbacks rápidos e temporários.*
