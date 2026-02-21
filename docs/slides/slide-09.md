# Aula 09 - Gerenciamento de Estado 🔄
## Fazendo o App Reagir

---

## Agenda de Hoje 📅

1. O que é Estado? <!-- .element: class="fragment" -->
2. Limitações do setState <!-- .element: class="fragment" -->
3. Introdução ao Provider <!-- .element: class="fragment" -->
4. ChangeNotifier e notifyListeners() <!-- .element: class="fragment" -->
5. Watch vs Read: Quando usar? <!-- .element: class="fragment" -->

---

## 1. O que é Estado? 🤔

- Estado é a "foto" do seu app em um momento. <!-- .element: class="fragment" -->
- "Está logado?" <!-- .element: class="fragment" -->
- "Quais itens estão no carrinho?" <!-- .element: class="fragment" -->
- "O botão está carregando?" <!-- .element: class="fragment" -->

---

## 2. Relembrando o setState() 🔴

- Simples e nativo. <!-- .element: class="fragment" -->
- Problema: "Prop Drilling" (Passar dados por 10 construtores). <!-- .element: class="fragment" -->
- Problema: Difícil compartilhar entre telas distantes. <!-- .element: class="fragment" -->

---

## 3. Gerenciamento Global 🌐

- Um lugar central de onde o estado "emana" para o resto do app. <!-- .element: class="fragment" -->

---

## 4. O Pacote Provider 📦

- O queridinho da comunidade. <!-- .element: class="fragment" -->
- Recomendações oficiais do Google. <!-- .element: class="fragment" -->
- Baseado em Injeção de Dependências. <!-- .element: class="fragment" -->

---

## 5. ChangeNotifier: O Motor ⚙️

- Uma classe que estende `ChangeNotifier`. <!-- .element: class="fragment" -->
- Possui variáveis e métodos que alteram essas variáveis. <!-- .element: class="fragment" -->

---

## 6. notifyListeners(): O Grito 📢

- Quando um dado muda, chamamos este método. <!-- .element: class="fragment" -->
- Ele avisa todos os Widgets interessados: "Hey, me redesenhe!". <!-- .element: class="fragment" -->

---

## 7. ChangeNotifierProvider: A Fonte ⛲

- Envolve um pedaço da árvore de widgets (geralmente o `MaterialApp`). <!-- .element: class="fragment" -->
- Disponibiliza o objeto de estado para todos os filhos. <!-- .element: class="fragment" -->

---

## 8. context.watch<T>() 👁️

- "Eu quero ver esse dado e me redesenhar sempre que ele mudar". <!-- .element: class="fragment" -->
- Usado dentro do método `build`. <!-- .element: class="fragment" -->

---

## 9. context.read<T>() 🖱️

- "Eu só quero acessar uma função desse objeto (ex: um clique)". <!-- .element: class="fragment" -->
- NÃO causa redesenho do widget. <!-- .element: class="fragment" -->

---

## 10. Consumer: Otimizando Performance ⚡

- Widget que redesenha apenas um pequeno pedaço da tela. <!-- .element: class="fragment" -->
- Evita reconstruir o Scaffold inteiro desnecessariamente. <!-- .element: class="fragment" -->

---

## 11. Multiprovider 🏗️

- O que fazer se tivermos vários estados (UserProvider, CartProvider)? <!-- .element: class="fragment" -->
- Organizamos em uma lista no topo do app. <!-- .element: class="fragment" -->

---

## 12. Outras Opções (BLoC e Riverpod) 🏛️

- BLoC: Focado em Streams (fluxos). <!-- .element: class="fragment" -->
- Riverpod: A evolução do Provider. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Estado é dado em movimento. <!-- .element: class="fragment" -->
- Provider desacopla a lógica da UI. <!-- .element: class="fragment" -->
- notifyListeners é o coração da reatividade. <!-- .element: class="fragment" -->

---

## Próxima Aula: APIs REST 📡

- Buscando dados na internet. <!-- .element: class="fragment" -->
- O mundo do Async/Await. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Um estado bem gerenciado torna o app previsível e fácil de testar."
