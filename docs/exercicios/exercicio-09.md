# Exercícios - Aula 09: Gerenciamento de Estado 🔄

### 🟢 Básicos (Fixação)

1. **Estado**: Dê 3 exemplos de dados em um aplicativo que seriam considerados "Estado" (que precisam ser atualizados na tela quando mudam).
2. **setState**: O que acontece se você mudar o valor de uma variável em um `StatefulWidget` mas esquecer de chamar o `setState()`?

### 🟡 Intermediários (Aplicação)

3. **Injeção**: Para que serve o widget `ChangeNotifierProvider`? Onde ele deve ser posicionado na árvore de widgets?
4. **Escuta**: Qual a diferença entre usar `context.watch<T>()` e `context.read<T>()` dentro de um método `build`?

### 🔴 Desafio (Pesquisa/Prática)

5. **Performance**: Pesquise sobre o widget `Consumer` do pacote Provider. Como ele ajuda a otimizar a performance do aplicativo em comparação com o uso do `watch` no topo do método build?