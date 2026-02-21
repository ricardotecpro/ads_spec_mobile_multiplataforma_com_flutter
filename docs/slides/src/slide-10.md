# Aula 10 - Consumo de APIs REST 📡
## Conectando seu App ao Mundo

---

## Agenda de Hoje 📅

1. O que é uma API REST? { .fragment }
2. Verbos HTTP e Status Codes { .fragment }
3. O Formato JSON { .fragment }
4. O Mundo Async/Await { .fragment }
5. Pacote http e Parsing { .fragment }

---

## 1. O que é uma API? 🌉

- Uma ponte entre o seu App e os dados no servidor. { .fragment }
- REST: O "dialeto" mais comum desta ponte. { .fragment }

---

## 2. Métodos HTTP 🛤️

- `GET`: Buscar dados. { .fragment }
- `POST`: Enviar novos dados. { .fragment }
- `PUT/PATCH`: Atualizar dados. { .fragment }
- `DELETE`: Remover dados. { .fragment }

---

## 3. Dialeto Universal: JSON 📜

- JavaScript Object Notation. { .fragment }
- Leve e fácil para o Dart entender. { .fragment }

---

## 4. Por que Assíncrono? ⏳

- A internet demora. { .fragment }
- Não podemos travar a tela (congelar o app) enquanto esperamos. { .fragment }

---

## 5. Future, Async e Await 🚀

- `Future`: Uma caixa que terá um presente (dado) no futuro. { .fragment }
- `async`: Diz que a função tem esperas. { .fragment }
- `await`: "Eu espero aqui, mas deixe a UI livre!". { .fragment }

---

## 6. O Pacote http 📦

- Adicione no `pubspec.yaml`. { .fragment }
- Permite fazer `http.get(url)`. { .fragment }

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

- `200`: Sucesso! { .fragment }
- `404`: Não encontrado. { .fragment }
- `500`: O servidor quebrou. { .fragment }

---

## 9. CircularProgressIndicator 🔄

- Sempre mostre que algo está acontecendo. { .fragment }
- UX é fundamental em chamadas de rede. { .fragment }

---

## 10. Tratamento de Erros (Try/Catch) 🛡️

- E se o usuário ficar sem Wi-Fi? { .fragment }
- O app não pode "crashar". { .fragment }

---

## 11. Debugando APIs 🐞

- Use o Postman ou Insomnia para testar as URLs antes de codar. { .fragment }

---

## 12. Ferramentas de Rede no DevTools 🛠️

- O Flutter possui ferramentas para ver o tráfego de dados em tempo real. { .fragment }

---

## Resumo da Aula ✅

- REST é o padrão da web. { .fragment }
- JSON é o formato de troca. { .fragment }
- Async/Await garante a fluidez do app. { .fragment }

---

## Próxima Aula: Persistência Local 💾

- SQLite e SharedPreferences. { .fragment }
- Salvando dados quando o celular desliga. { .fragment }

---

## Dúvidas? 🤔

> "A internet é o banco de dados infinito do seu aplicativo."