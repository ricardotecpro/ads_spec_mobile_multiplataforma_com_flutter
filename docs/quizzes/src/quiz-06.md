# Quiz 06 - Componentes Visuais 🖼️

1. Qual propriedade do widget `Text` usamos para mudar a cor e o tamanho da fonte?
    - [ ] font:
    - [ ] theme:
    - [x] style: TextStyle(...)
    - [ ] colorSettings:
    *Explicação: Toda a estilização de texto é concentrada na classe `TextStyle`.*

2. Como exibimos uma imagem vinda de uma URL da internet?
    - [ ] Image.asset(...)
    - [x] Image.network(...)
    - [ ] Image.file(...)
    - [ ] Image.url(...)
    *Explicação: `Image.network` é o construtor específico para carregar imagens via protocolo HTTP.*

3. Qual o widget de botão padrão que possui cor de fundo e sombra no Material 3?
    - [ ] TextButton
    - [ ] OutlinedButton
    - [x] ElevatedButton
    - [ ] FlatButton
    *Explicação: O `ElevatedButton` é o botão de destaque principal na hierarquia visual.*

4. Para que serve o widget `AppBar`?
    - [ ] Para mostrar propagandas.
    - [x] Para exibir o título da página e ações no topo da tela.
    - [ ] Para salvar dados no celular.
    - [ ] Para mudar o ícone do app.
    *Explicação: A `AppBar` é a barra superior de navegação e título.*

5. Qual widget usamos para exibir ícones prontos do sistema?
    - [ ] Img()
    - [ ] SVG()
    - [x] Icon(Icons.nome_do_icone)
    - [ ] MaterialDesign()
    *Explicação: O Flutter já vem com a biblioteca `Material Icons` integrada.*

6. Qual parâmetro de um botão define o que acontece quando ele é clicado?
    - [ ] onClick:
    - [x] onPressed:
    - [ ] tap:
    - [ ] execute:
    *Explicação: No Flutter, a função de callback de clique é quase sempre chamada de `onPressed`.*

7. Como transformamos qualquer widget em um botão clicável?
    - [ ] Envolvendo-o em um `Scaffold`.
    - [x] Envolvendo-o em um `GestureDetector` ou `InkWell`.
    - [ ] Usando o comando `makeClickable: true`.
    - [ ] Mudando a cor para azul.
    *Explicação: `InkWell` adiciona o efeito visual de "toque" (ripple), enquanto `GestureDetector` captura apenas o gesto.*

8. Qual o papel do widget `CircleAvatar`?
    - [ ] Criar um botão redondo.
    - [x] Exibir uma imagem ou texto em formato circular, comum para fotos de perfil.
    - [ ] Desenhar círculos matemáticos na tela.
    - [ ] Criar um relógio.
    *Explicação: Ele é o widget padrão para representar avatares de usuários.*

9. O que o widget `Divider` faz?
    - [ ] Divide o valor de dois números.
    - [x] Desenha uma linha horizontal fina para separar conteúdos.
    - [ ] Quebra a interface em duas.
    - [ ] Fecha o aplicativo.
    *Explicação: É um componente visual de separação.*

10. Como definimos um ícone que fica no final da `AppBar`?
    - [ ] Usando o parâmetro `leading`.
    - [ ] Usando o parâmetro `title`.
    - [x] Usando a lista `actions: []`.
    - [ ] Usando `trailing`.
    *Explicação: `leading` fica no início (esquerda), `title` no meio e `actions` no final (direita).*
