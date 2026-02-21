# Aula 07 - Navegação entre Telas 🛣️
## Viajando pelo seu Aplicativo

---

## Agenda de Hoje 📅

1. O Conceito de Pilha (Stack) { .fragment }
2. Navigator: Push e Pop { .fragment }
3. Rotas Nomeadas { .fragment }
4. Passagem de Parâmetros { .fragment }
5. MaterialPageRoute { .fragment }

---

## 1. A Pilha de Pratos 📚

- Navigator é como uma pilha de pratos (telas). { .fragment }
- Você coloca um prato em cima (Push). { .fragment }
- Você tira o prato de cima (Pop). { .fragment }

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

- Remove a tela atual. { .fragment }
- Volta para a anterior automaticamente. { .fragment }

---

## 4. Rotas Nomeadas 🏷️

- Definimos um "dicionário" de URLs. { .fragment }
- `Navigator.pushNamed(context, '/detalhes');` { .fragment }

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

- A forma mais simples. { .fragment }
- `TelaDetalhes(produto: meuProduto)` { .fragment }

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

- Remove a tela atual e coloca a nova. { .fragment }
- Ideal para Splash Screens e Fluxos de Login. { .fragment }

---

## 9. Limpando a Pilha (pushAndRemoveUntil) 🧹

- Limpa todo o histórico. { .fragment }
- Útil para o botão de "Sair/Logout". { .fragment }

---

## 10. Navegação no iOS vs Android 🍎🤖

- Flutter cuida das animações nativas. { .fragment }
- Deslizar lateral no iOS, Fade/Subida no Android. { .fragment }

---

## 11. O Botão "Voltar" Físico (Android) ⬅️

- Gerenciado automaticamente pelo Navigator. { .fragment }

---

## 12. ModalRoute: Recuperando Dados 🎣

- `ModalRoute.of(context)!.settings.arguments` { .fragment }

---

## Resumo da Aula ✅

- Navegar é gerenciar uma pilha. { .fragment }
- Rotas nomeadas organizam o código. { .fragment }
- Push e Pop são os comandos fundamentais. { .fragment }

---

## Próxima Aula: Formulários 📝

- Colhendo dados do usuário. { .fragment }
- Validação e Teclado. { .fragment }

---

## Dúvidas? 🤔

> "Navegar não é apenas trocar de tela, é guiar a jornada do usuário."
