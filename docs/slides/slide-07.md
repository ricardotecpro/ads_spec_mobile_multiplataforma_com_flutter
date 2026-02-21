# Aula 07 - Navegação entre Telas 🛣️
## Viajando pelo seu Aplicativo

---

## Agenda de Hoje 📅

1. O Conceito de Pilha (Stack) <!-- .element: class="fragment" -->
2. Navigator: Push e Pop <!-- .element: class="fragment" -->
3. Rotas Nomeadas <!-- .element: class="fragment" -->
4. Passagem de Parâmetros <!-- .element: class="fragment" -->
5. MaterialPageRoute <!-- .element: class="fragment" -->

---

## 1. A Pilha de Pratos 📚

- Navigator é como uma pilha de pratos (telas). <!-- .element: class="fragment" -->
- Você coloca um prato em cima (Push). <!-- .element: class="fragment" -->
- Você tira o prato de cima (Pop). <!-- .element: class="fragment" -->

---

## 2. Navigator.push() ➡️

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => TelaB()),
);
```

---

## 3. Navigator.pop() ⬅️

- Remove a tela atual. <!-- .element: class="fragment" -->
- Volta para a anterior automaticamente. <!-- .element: class="fragment" -->

---

## 4. Rotas Nomeadas 🏷️

- Definimos um "dicionário" de URLs. <!-- .element: class="fragment" -->
- `Navigator.pushNamed(context, '/detalhes');` <!-- .element: class="fragment" -->

---

## 5. Configurando Rotas 🛠️

```dart
MaterialApp(
  routes: {
    '/': (context) => Home(),
    '/config': (context) => Config(),
  }
)
```

---

## 6. Passando Dados no Construtor 📦

- A forma mais simples. <!-- .element: class="fragment" -->
- `TelaDetalhes(produto: meuProduto)` <!-- .element: class="fragment" -->

---

## 7. Passando Dados via Arguments 🚚

```dart
Navigator.pushNamed(
  context, 
  '/detalhes', 
  arguments: idDoProduto
);
```

---

## 8. Substituindo Telas (pushReplacement) 🔄

- Remove a tela atual e coloca a nova. <!-- .element: class="fragment" -->
- Ideal para Splash Screens e Fluxos de Login. <!-- .element: class="fragment" -->

---

## 9. Limpando a Pilha (pushAndRemoveUntil) 🧹

- Limpa todo o histórico. <!-- .element: class="fragment" -->
- Útil para o botão de "Sair/Logout". <!-- .element: class="fragment" -->

---

## 10. Navegação no iOS vs Android 🍎🤖

- Flutter cuida das animações nativas. <!-- .element: class="fragment" -->
- Deslizar lateral no iOS, Fade/Subida no Android. <!-- .element: class="fragment" -->

---

## 11. O Botão "Voltar" Físico (Android) ⬅️

- Gerenciado automaticamente pelo Navigator. <!-- .element: class="fragment" -->

---

## 12. ModalRoute: Recuperando Dados 🎣

- `ModalRoute.of(context)!.settings.arguments` <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Navegar é gerenciar uma pilha. <!-- .element: class="fragment" -->
- Rotas nomeadas organizam o código. <!-- .element: class="fragment" -->
- Push e Pop são os comandos fundamentais. <!-- .element: class="fragment" -->

---

## Próxima Aula: Formulários 📝

- Colhendo dados do usuário. <!-- .element: class="fragment" -->
- Validação e Teclado. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Navegar não é apenas trocar de tela, é guiar a jornada do usuário."
