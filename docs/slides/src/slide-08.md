# Aula 08 - Formulários e Validação 📝
## Interagindo e Colhendo Dados

---

## Agenda de Hoje 📅

1. TextField e Input ⌨️
2. TextEditingController { .fragment }
3. O Widget Form { .fragment }
4. Validação de Dados { .fragment }
5. Tipos de Teclado { .fragment }

---

## 1. TextField: A porta de entrada ✍️

- Captura o que o usuário digita. { .fragment }
- Customizável via `InputDecoration`. { .fragment }

---

## 2. TextEditingController: O "Controle Remoto" 🕹️

- Serve para ler o texto do campo. { .fragment }
- Serve para limpar o campo programaticamente. { .fragment }

---

## 3. TextField vs TextFormField ⚔️

- `TextFormField` é uma versão tunada que entende de validação e formulários. { .fragment }

---

## 4. O Widget Form 🧱

- Envelopa vários campos. { .fragment }
- Permite validar todos de uma vez usando uma `GlobalKey`. { .fragment }

---

## 5. GlobalKey: Identificando o Form 🔑

```dart
final _formKey = GlobalKey<FormState>();
// ...
if (_formKey.currentState!.validate()) {
  // Dados válidos!
}
```

---

## 6. O parâmetro validator 🛡️

- Uma função que retorna uma mensagem de erro se o dado for inválido. { .fragment }
- Retorna `null` se tudo estiver OK. { .fragment }

---

## 7. Dicas Visuais (Hint e Label) 💡

- `labelText`: O nome do campo que "sobe". { .fragment }
- `hintText`: O exemplo (placeholder). { .fragment }

---

## 8. obscureText: Campo de Senha 🔒

- Esconde os caracteres com círculos ou asteriscos. { .fragment }

---

## 9. teclados Otimizados (TextInputType) ⌨️

- `number`: Apenas números. { .fragment }
- `emailAddress`: Inclui o "@". { .fragment }
- `phone`: Teclado numérico de ligação. { .fragment }

---

## 10. Gerenciando o Foco 🔎

- Mudar para o próximo campo ao apertar "Enter". { .fragment }
- `FocusNode` para controle avançado. { .fragment }

---

## 11. MaxLines e MaxLength 📏

- Limitar a quantidade de caracteres. { .fragment }
- Permitir múltiplas linhas para comentários. { .fragment }

---

## 12. Máscaras de Input 🎭

- CPF: `###.###.###-##` { .fragment }
- Melhorar a experiência do usuário. { .fragment }

---

## Resumo da Aula ✅

- Controllers capturam dados. { .fragment }
- Forms validam a consistência. { .fragment }
- Teclados certos ajudam o usuário. { .fragment }

---

## Próxima Aula: Gerenciamento de Estado 🔄

-setState e Provider. { .fragment }
- Reatividade na prática. { .fragment }

---

## Dúvidas? 🤔

> "Um formulário bem validado é a primeira linha de defesa contra dados ruins."