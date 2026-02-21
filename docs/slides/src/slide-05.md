# Aula 05 - Layouts e Organização Visual 🎨
## Dominando Column, Row e Container

---

## Agenda de Hoje 📅

1. Eixos de Alinhamento { .fragment }
2. Column e Row { .fragment }
3. O Poder do Container { .fragment }
4. Padding e Margin { .fragment }
5. Widgets Flexíveis (Expanded) { .fragment }

---

## 1. Pensando em Caixas 📦

- Interfaces são coleções de caixas. { .fragment }
- Elas podem estar uma ao lado da outra ou uma sobre a outra. { .fragment }

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

- No `Column`: Alinha verticalmente (Início, Centralizado, Fim, Espaçamento). { .fragment }
- No `Row`: Alinha horizontalmente. { .fragment }

---

## 5. CrossAxisAlignment ⚔️

- O eixo cruzado (oposto ao principal). { .fragment }
- No `Column`: Alinha horizontalmente (Esticar, Centralizar). { .fragment }

---

## 6. Container: O Canivete Suíço 🛠️

- Permite definir: Cor, Borda, Tamanho, Alinhamento. { .fragment }

---

## 7. Espaçamentos: Padding 👕

- Espaço interno entre a borda e o conteúdo. { .fragment }
- `EdgeInsets.all(16)` { .fragment }

---

## 8. Espaçamentos: Margin 🧱

- Espaço externo entre o widget e seus vizinhos. { .fragment }

---

## 9. Expanded: Ocupando Espaço ↔️

- Força o widget a preencher o espaço restante no eixo principal. { .fragment }
- Útil para criar layouts flexíveis. { .fragment }

---

## 10. Diferença entre Expanded e Flexible ⚖️

- `Expanded`: Sempre preenche. { .fragment }
- `Flexible`: Preenche se necessário, mas respeita o tamanho do filho. { .fragment }

---

## 11. Estilizando com BoxDecoration 🎨

- Bordas arredondadas. { .fragment }
- Sombras (BoxShadow). { .fragment }
- Gradientes de cor. { .fragment }

---

## 12. Tamanhos Infinitos? ⚠️

- `double.infinity` faz o widget tentar ser o maior possível. { .fragment }
- Cuidado com erros de "Layout Overflow"! { .fragment }

---

## Resumo da Aula ✅

- Column e Row organizam a estrutura. { .fragment }
- Container e Padding cuidam do estilo. { .fragment }
- Expanded garante a flexibilidade. { .fragment }

---

## Próxima Aula: Componentes UI 🖼️

- Text, Image e Buttons. { .fragment }
- Deixando o app com cara de Material Design. { .fragment }

---

## Dúvidas? 🤔

> "Layout não é sobre onde os elementos estão, mas sobre como eles se adaptam."
