# Quiz 05 - Layouts e Organização Visual 🎨

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual widget usamos para empilhar outros widgets verticalmente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `Column` organiza seus filhos de cima para baixo em uma linha vertical.">Row</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A `Column` organiza seus filhos de cima para baixo em uma linha vertical.">Column</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `Column` organiza seus filhos de cima para baixo em uma linha vertical.">Stack</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `Column` organiza seus filhos de cima para baixo em uma linha vertical.">ListView</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. E para alinhar elementos horizontalmente (lado a lado)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `Row` distribui seus filhos da esquerda para a direita.">Column</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `Row` distribui seus filhos da esquerda para a direita.">Center</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A `Row` distribui seus filhos da esquerda para a direita.">Row</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A `Row` distribui seus filhos da esquerda para a direita.">Padding</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual propriedade da `Column` alinha os itens no eixo vertical (eixo principal)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No `Column`, o eixo principal (`main`) é o vertical.">crossAxisAlignment</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No `Column`, o eixo principal (`main`) é o vertical.">mainAxisAlignment</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No `Column`, o eixo principal (`main`) é o vertical.">alignVertical</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No `Column`, o eixo principal (`main`) é o vertical.">spacing</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Para que serve o widget `Container`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Container` é um canivete suíço para estilização (bordas, cores, tamanhos).">Apenas para guardar texto.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `Container` é um canivete suíço para estilização (bordas, cores, tamanhos).">Para combinar pintura, posicionamento e dimensionamento de widgets.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Container` é um canivete suíço para estilização (bordas, cores, tamanhos).">Para criar listas infinitas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Container` é um canivete suíço para estilização (bordas, cores, tamanhos).">Para tocar músicas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a diferença entre Padding e Margin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O padding afasta o conteúdo das bordas internas da caixa, enquanto a margem afasta a caixa de outros widgets externos.">Não há diferença.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O padding afasta o conteúdo das bordas internas da caixa, enquanto a margem afasta a caixa de outros widgets externos.">Padding é espaço interno; Margin é espaço externo ao widget.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O padding afasta o conteúdo das bordas internas da caixa, enquanto a margem afasta a caixa de outros widgets externos.">Margin é apenas para cores.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O padding afasta o conteúdo das bordas internas da caixa, enquanto a margem afasta a caixa de outros widgets externos.">Padding só funciona em botões.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Como fazemos para um widget ocupar todo o espaço restante em uma `Row` ou `Column`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Expanded` força o widget a se expandir para preencher o espaço disponível no eixo principal.">Colocando width: double.infinity.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `Expanded` força o widget a se expandir para preencher o espaço disponível no eixo principal.">Envolvendo-o no widget `Expanded`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Expanded` força o widget a se expandir para preencher o espaço disponível no eixo principal.">Usando um `Container` vazio.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `Expanded` força o widget a se expandir para preencher o espaço disponível no eixo principal.">Aumentando o tamanho da fonte.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual widget permite colocar elementos uns sobre os outros (em camadas)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O widget `Stack` (Pilha) sobrepõe widgets na ordem em que são declarados.">Column</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O widget `Stack` (Pilha) sobrepõe widgets na ordem em que são declarados.">Row</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O widget `Stack` (Pilha) sobrepõe widgets na ordem em que são declarados.">Stack</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O widget `Stack` (Pilha) sobrepõe widgets na ordem em que são declarados.">Layer</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que o `MainAxisAlignment.spaceBetween` faz?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele maximiza o espaço entre os elementos dentro do eixo principal.">Coloca todos os itens no centro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele maximiza o espaço entre os elementos dentro do eixo principal.">Coloca o primeiro item no início, o último no fim e distribui o espaço entre os demais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele maximiza o espaço entre os elementos dentro do eixo principal.">Deleta o espaço entre os itens.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele maximiza o espaço entre os elementos dentro do eixo principal.">Cria uma borda preta.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual widget fornece rolagem automática quando o conteúdo ultrapassa o tamanho da tela?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem um widget de scroll, o Flutter mostra um erro de "Overflow" (faixas amarelas e pretas) se o conteúdo for maior que a tela.">Scaffold</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem um widget de scroll, o Flutter mostra um erro de "Overflow" (faixas amarelas e pretas) se o conteúdo for maior que a tela.">Column</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem um widget de scroll, o Flutter mostra um erro de "Overflow" (faixas amarelas e pretas) se o conteúdo for maior que a tela.">SingleChildScrollView</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem um widget de scroll, o Flutter mostra um erro de "Overflow" (faixas amarelas e pretas) se o conteúdo for maior que a tela.">OverflowBox</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No widget `Container`, como definimos uma borda arredondada?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estilização avançada do Container é feita via `BoxDecoration`.">Usando o comando `borderRadius` direto no Container.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Estilização avançada do Container é feita via `BoxDecoration`.">Através da propriedade `decoration: BoxDecoration(...)`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estilização avançada do Container é feita via `BoxDecoration`.">Usando o widget `CircleAvatar`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estilização avançada do Container é feita via `BoxDecoration`.">Não é possível arredondar bordas.</div>
  <div class="quiz-feedback"></div>
</div>
