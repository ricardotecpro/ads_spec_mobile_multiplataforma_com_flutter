# Aula 09 - Gerenciamento de Estado 🔄
## Fazendo o App Reagir

---

## Agenda de Hoje 📅

1. O que é Estado? { .fragment }
2. Limitações do setState { .fragment }
3. Introdução ao Provider { .fragment }
4. ChangeNotifier e notifyListeners() { .fragment }
5. Watch vs Read: Quando usar? { .fragment }

---

## 1. O que é Estado? 🤔

- Estado é a "foto" do seu app em um momento. { .fragment }
- "Está logado?" { .fragment }
- "Quais itens estão no carrinho?" { .fragment }
- "O botão está carregando?" { .fragment }

---

## 2. Relembrando o setState() 🔴

- Simples e nativo. { .fragment }
- Problema: "Prop Drilling" (Passar dados por 10 construtores). { .fragment }
- Problema: Difícil compartilhar entre telas distantes. { .fragment }

---

## 3. Gerenciamento Global 🌐

- Um lugar central de onde o estado "emana" para o resto do app. { .fragment }

---

## 4. O Pacote Provider 📦

- O queridinho da comunidade. { .fragment }
- Recomendações oficiais do Google. { .fragment }
- Baseado em Injeção de Dependências. { .fragment }

---

## 5. ChangeNotifier: O Motor ⚙️

- Uma classe que estende `ChangeNotifier`. { .fragment }
- Possui variáveis e métodos que alteram essas variáveis. { .fragment }

---

## 6. notifyListeners(): O Grito 📢

- Quando um dado muda, chamamos este método. { .fragment }
- Ele avisa todos os Widgets interessados: "Hey, me redesenhe!". { .fragment }

---

## 7. ChangeNotifierProvider: A Fonte ⛲

- Envolve um pedaço da árvore de widgets (geralmente o `MaterialApp`). { .fragment }
- Disponibiliza o objeto de estado para todos os filhos. { .fragment }

---

## 8. context.watch<T>() 👁️

- "Eu quero ver esse dado e me redesenhar sempre que ele mudar". { .fragment }
- Usado dentro do método `build`. { .fragment }

---

## 9. context.read<T>() 🖱️

- "Eu só quero acessar uma função desse objeto (ex: um clique)". { .fragment }
- NÃO causa redesenho do widget. { .fragment }

---

## 10. Consumer: Otimizando Performance ⚡

- Widget que redesenha apenas um pequeno pedaço da tela. { .fragment }
- Evita reconstruir o Scaffold inteiro desnecessariamente. { .fragment }

---

## 11. Multiprovider 🏗️

- O que fazer se tivermos vários estados (UserProvider, CartProvider)? { .fragment }
- Organizamos em uma lista no topo do app. { .fragment }

---

## 12. Outras Opções (BLoC e Riverpod) 🏛️

- BLoC: Focado em Streams (fluxos). { .fragment }
- Riverpod: A evolução do Provider. { .fragment }

---

## Resumo da Aula ✅

- Estado é dado em movimento. { .fragment }
- Provider desacopla a lógica da UI. { .fragment }
- notifyListeners é o coração da reatividade. { .fragment }

---

## Próxima Aula: APIs REST 📡

- Buscando dados na internet. { .fragment }
- O mundo do Async/Await. { .fragment }

---

## Dúvidas? 🤔

> "Um estado bem gerenciado torna o app previsível e fácil de testar."
