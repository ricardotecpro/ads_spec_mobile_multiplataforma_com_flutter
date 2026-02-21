# Aula 05 - Layouts e Organização Visual 🎨
## Dominando Column, Row e Container

---

## Agenda de Hoje 📅

1. Eixos de Alinhamento <!-- .element: class="fragment" -->
2. Column e Row <!-- .element: class="fragment" -->
3. O Poder do Container <!-- .element: class="fragment" -->
4. Padding e Margin <!-- .element: class="fragment" -->
5. Widgets Flexíveis (Expanded) <!-- .element: class="fragment" -->

---

## 1. Pensando em Caixas 📦

- Interfaces são coleções de caixas. <!-- .element: class="fragment" -->
- Elas podem estar uma ao lado da outra ou uma sobre a outra. <!-- .element: class="fragment" -->

---

## 2. Column (Vertical) ↕️

```dart
Column(
  children: [
    Text("Item 1"),
    Text("Item 2"),
  ],
)
```

---

## 3. Row (Horizontal) ↔️

```dart
Row(
  children: [
    Icon(Icons.star),
    Text("Avaliação"),
  ],
)
```

---

## 4. MainAxisAlignment 🏹

- No `Column`: Alinha verticalmente (Início, Centralizado, Fim, Espaçamento). <!-- .element: class="fragment" -->
- No `Row`: Alinha horizontalmente. <!-- .element: class="fragment" -->

---

## 5. CrossAxisAlignment ⚔️

- O eixo cruzado (oposto ao principal). <!-- .element: class="fragment" -->
- No `Column`: Alinha horizontalmente (Esticar, Centralizar). <!-- .element: class="fragment" -->

---

## 6. Container: O Canivete Suíço 🛠️

- Permite definir: Cor, Borda, Tamanho, Alinhamento. <!-- .element: class="fragment" -->

---

## 7. Espaçamentos: Padding 👕

- Espaço interno entre a borda e o conteúdo. <!-- .element: class="fragment" -->
- `EdgeInsets.all(16)` <!-- .element: class="fragment" -->

---

## 8. Espaçamentos: Margin 🧱

- Espaço externo entre o widget e seus vizinhos. <!-- .element: class="fragment" -->

---

## 9. Expanded: Ocupando Espaço ↔️

- Força o widget a preencher o espaço restante no eixo principal. <!-- .element: class="fragment" -->
- Útil para criar layouts flexíveis. <!-- .element: class="fragment" -->

---

## 10. Diferença entre Expanded e Flexible ⚖️

- `Expanded`: Sempre preenche. <!-- .element: class="fragment" -->
- `Flexible`: Preenche se necessário, mas respeita o tamanho do filho. <!-- .element: class="fragment" -->

---

## 11. Estilizando com BoxDecoration 🎨

- Bordas arredondadas. <!-- .element: class="fragment" -->
- Sombras (BoxShadow). <!-- .element: class="fragment" -->
- Gradientes de cor. <!-- .element: class="fragment" -->

---

## 12. Tamanhos Infinitos? ⚠️

- `double.infinity` faz o widget tentar ser o maior possível. <!-- .element: class="fragment" -->
- Cuidado com erros de "Layout Overflow"! <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Column e Row organizam a estrutura. <!-- .element: class="fragment" -->
- Container e Padding cuidam do estilo. <!-- .element: class="fragment" -->
- Expanded garante a flexibilidade. <!-- .element: class="fragment" -->

---

## Próxima Aula: Componentes UI 🖼️

- Text, Image e Buttons. <!-- .element: class="fragment" -->
- Deixando o app com cara de Material Design. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Layout não é sobre onde os elementos estão, mas sobre como eles se adaptam."
