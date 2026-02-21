# Aula 08 - Formulários e Validação 📝
## Interagindo e Colhendo Dados

---

## Agenda de Hoje 📅

1. TextField e Input ⌨️
2. TextEditingController <!-- .element: class="fragment" -->
3. O Widget Form <!-- .element: class="fragment" -->
4. Validação de Dados <!-- .element: class="fragment" -->
5. Tipos de Teclado <!-- .element: class="fragment" -->

---

## 1. TextField: A porta de entrada ✍️

- Captura o que o usuário digita. <!-- .element: class="fragment" -->
- Customizável via `InputDecoration`. <!-- .element: class="fragment" -->

---

## 2. TextEditingController: O "Controle Remoto" 🕹️

- Serve para ler o texto do campo. <!-- .element: class="fragment" -->
- Serve para limpar o campo programaticamente. <!-- .element: class="fragment" -->

---

## 3. TextField vs TextFormField ⚔️

- `TextFormField` é uma versão tunada que entende de validação e formulários. <!-- .element: class="fragment" -->

---

## 4. O Widget Form 🧱

- Envelopa vários campos. <!-- .element: class="fragment" -->
- Permite validar todos de uma vez usando uma `GlobalKey`. <!-- .element: class="fragment" -->

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

- Uma função que retorna uma mensagem de erro se o dado for inválido. <!-- .element: class="fragment" -->
- Retorna `null` se tudo estiver OK. <!-- .element: class="fragment" -->

---

## 7. Dicas Visuais (Hint e Label) 💡

- `labelText`: O nome do campo que "sobe". <!-- .element: class="fragment" -->
- `hintText`: O exemplo (placeholder). <!-- .element: class="fragment" -->

---

## 8. obscureText: Campo de Senha 🔒

- Esconde os caracteres com círculos ou asteriscos. <!-- .element: class="fragment" -->

---

## 9. teclados Otimizados (TextInputType) ⌨️

- `number`: Apenas números. <!-- .element: class="fragment" -->
- `emailAddress`: Inclui o "@". <!-- .element: class="fragment" -->
- `phone`: Teclado numérico de ligação. <!-- .element: class="fragment" -->

---

## 10. Gerenciando o Foco 🔎

- Mudar para o próximo campo ao apertar "Enter". <!-- .element: class="fragment" -->
- `FocusNode` para controle avançado. <!-- .element: class="fragment" -->

---

## 11. MaxLines e MaxLength 📏

- Limitar a quantidade de caracteres. <!-- .element: class="fragment" -->
- Permitir múltiplas linhas para comentários. <!-- .element: class="fragment" -->

---

## 12. Máscaras de Input 🎭

- CPF: `###.###.###-##` <!-- .element: class="fragment" -->
- Melhorar a experiência do usuário. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Controllers capturam dados. <!-- .element: class="fragment" -->
- Forms validam a consistência. <!-- .element: class="fragment" -->
- Teclados certos ajudam o usuário. <!-- .element: class="fragment" -->

---

## Próxima Aula: Gerenciamento de Estado 🔄

-setState e Provider. <!-- .element: class="fragment" -->
- Reatividade na prática. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Um formulário bem validado é a primeira linha de defesa contra dados ruins."