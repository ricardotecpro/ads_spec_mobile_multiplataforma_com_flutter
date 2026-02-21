# Aula 10 - Consumo de APIs REST 📡
## Conectando seu App ao Mundo

---

## Agenda de Hoje 📅

1. O que é uma API REST? <!-- .element: class="fragment" -->
2. Verbos HTTP e Status Codes <!-- .element: class="fragment" -->
3. O Formato JSON <!-- .element: class="fragment" -->
4. O Mundo Async/Await <!-- .element: class="fragment" -->
5. Pacote http e Parsing <!-- .element: class="fragment" -->

---

## 1. O que é uma API? 🌉

- Uma ponte entre o seu App e os dados no servidor. <!-- .element: class="fragment" -->
- REST: O "dialeto" mais comum desta ponte. <!-- .element: class="fragment" -->

---

## 2. Métodos HTTP 🛤️

- `GET`: Buscar dados. <!-- .element: class="fragment" -->
- `POST`: Enviar novos dados. <!-- .element: class="fragment" -->
- `PUT/PATCH`: Atualizar dados. <!-- .element: class="fragment" -->
- `DELETE`: Remover dados. <!-- .element: class="fragment" -->

---

## 3. Dialeto Universal: JSON 📜

- JavaScript Object Notation. <!-- .element: class="fragment" -->
- Leve e fácil para o Dart entender. <!-- .element: class="fragment" -->

---

## 4. Por que Assíncrono? ⏳

- A internet demora. <!-- .element: class="fragment" -->
- Não podemos travar a tela (congelar o app) enquanto esperamos. <!-- .element: class="fragment" -->

---

## 5. Future, Async e Await 🚀

- `Future`: Uma caixa que terá um presente (dado) no futuro. <!-- .element: class="fragment" -->
- `async`: Diz que a função tem esperas. <!-- .element: class="fragment" -->
- `await`: "Eu espero aqui, mas deixe a UI livre!". <!-- .element: class="fragment" -->

---

## 6. O Pacote http 📦

- Adicione no `pubspec.yaml`. <!-- .element: class="fragment" -->
- Permite fazer `http.get(url)`. <!-- .element: class="fragment" -->

---

## 7. Decodificando o JSON 🔓

```dart
import 'dart:convert';
// ...
var dados = jsonDecode(response.body);
print(dados['logradouro']);
```

---

## 8. Status Codes: O que aconteceu? 🚦

- `200`: Sucesso! <!-- .element: class="fragment" -->
- `404`: Não encontrado. <!-- .element: class="fragment" -->
- `500`: O servidor quebrou. <!-- .element: class="fragment" -->

---

## 9. CircularProgressIndicator 🔄

- Sempre mostre que algo está acontecendo. <!-- .element: class="fragment" -->
- UX é fundamental em chamadas de rede. <!-- .element: class="fragment" -->

---

## 10. Tratamento de Erros (Try/Catch) 🛡️

- E se o usuário ficar sem Wi-Fi? <!-- .element: class="fragment" -->
- O app não pode "crashar". <!-- .element: class="fragment" -->

---

## 11. Debugando APIs 🐞

- Use o Postman ou Insomnia para testar as URLs antes de codar. <!-- .element: class="fragment" -->

---

## 12. Ferramentas de Rede no DevTools 🛠️

- O Flutter possui ferramentas para ver o tráfego de dados em tempo real. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- REST é o padrão da web. <!-- .element: class="fragment" -->
- JSON é o formato de troca. <!-- .element: class="fragment" -->
- Async/Await garante a fluidez do app. <!-- .element: class="fragment" -->

---

## Próxima Aula: Persistência Local 💾

- SQLite e SharedPreferences. <!-- .element: class="fragment" -->
- Salvando dados quando o celular desliga. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "A internet é o banco de dados infinito do seu aplicativo."