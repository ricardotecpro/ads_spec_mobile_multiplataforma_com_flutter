# Quiz 05 - Layouts e Organização Visual 🎨

1. Qual widget usamos para empilhar outros widgets verticalmente?
    - [ ] Row
    - [x] Column
    - [ ] Stack
    - [ ] ListView
    *Explicação: A `Column` organiza seus filhos de cima para baixo em uma linha vertical.*

2. E para alinhar elementos horizontalmente (lado a lado)?
    - [ ] Column
    - [ ] Center
    - [x] Row
    - [ ] Padding
    *Explicação: A `Row` distribui seus filhos da esquerda para a direita.*

3. Qual propriedade da `Column` alinha os itens no eixo vertical (eixo principal)?
    - [ ] crossAxisAlignment
    - [x] mainAxisAlignment
    - [ ] alignVertical
    - [ ] spacing
    *Explicação: No `Column`, o eixo principal (`main`) é o vertical.*

4. Para que serve o widget `Container`?
    - [ ] Apenas para guardar texto.
    - [x] Para combinar pintura, posicionamento e dimensionamento de widgets.
    - [ ] Para criar listas infinitas.
    - [ ] Para tocar músicas.
    *Explicação: O `Container` é um canivete suíço para estilização (bordas, cores, tamanhos).*

5. Qual a diferença entre Padding e Margin?
    - [ ] Não há diferença.
    - [x] Padding é espaço interno; Margin é espaço externo ao widget.
    - [ ] Margin é apenas para cores.
    - [ ] Padding só funciona em botões.
    *Explicação: O padding afasta o conteúdo das bordas internas da caixa, enquanto a margem afasta a caixa de outros widgets externos.*

6. Como fazemos para um widget ocupar todo o espaço restante em uma `Row` ou `Column`?
    - [ ] Colocando width: double.infinity.
    - [x] Envolvendo-o no widget `Expanded`.
    - [ ] Usando um `Container` vazio.
    - [ ] Aumentando o tamanho da fonte.
    *Explicação: O `Expanded` força o widget a se expandir para preencher o espaço disponível no eixo principal.*

7. Qual widget permite colocar elementos uns sobre os outros (em camadas)?
    - [ ] Column
    - [ ] Row
    - [x] Stack
    - [ ] Layer
    *Explicação: O widget `Stack` (Pilha) sobrepõe widgets na ordem em que são declarados.*

8. O que o `MainAxisAlignment.spaceBetween` faz?
    - [ ] Coloca todos os itens no centro.
    - [x] Coloca o primeiro item no início, o último no fim e distribui o espaço entre os demais.
    - [ ] Deleta o espaço entre os itens.
    - [ ] Cria uma borda preta.
    *Explicação: Ele maximiza o espaço entre os elementos dentro do eixo principal.*

9. Qual widget fornece rolagem automática quando o conteúdo ultrapassa o tamanho da tela?
    - [ ] Scaffold
    - [ ] Column
    - [x] SingleChildScrollView
    - [ ] OverflowBox
    *Explicação: Sem um widget de scroll, o Flutter mostra um erro de "Overflow" (faixas amarelas e pretas) se o conteúdo for maior que a tela.*

10. No widget `Container`, como definimos uma borda arredondada?
    - [ ] Usando o comando `borderRadius` direto no Container.
    - [x] Através da propriedade `decoration: BoxDecoration(...)`.
    - [ ] Usando o widget `CircleAvatar`.
    - [ ] Não é possível arredondar bordas.
    *Explicação: Estilização avançada do Container é feita via `BoxDecoration`.*