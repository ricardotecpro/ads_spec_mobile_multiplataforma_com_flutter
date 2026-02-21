# Aula 12 - Organização Profissional 🏛️
## De Código para Engenharia

---

## Agenda de Hoje 📅

1. Por que Organizar? <!-- .element: class="fragment" -->
2. Clean Architecture Simplificada <!-- .element: class="fragment" -->
3. Models, Services e Providers <!-- .element: class="fragment" -->
4. O Princípio DRY <!-- .element: class="fragment" -->
5. Boas Práticas e Linter <!-- .element: class="fragment" -->

---

## 1. O Código "Espaguete" 🍝

- Tudo no mesmo arquivo. <!-- .element: class="fragment" -->
- Impossível de testar. <!-- .element: class="fragment" -->
- Um bug corrigido gera três novos bugs. <!-- .element: class="fragment" -->

---

## 2. Separação de Preocupações ✂️

- A Tela não deve saber como o Banco de Dados funciona. <!-- .element: class="fragment" -->
- O Modelo não deve saber como ele é desenhado. <!-- .element: class="fragment" -->

---

## 3. A Camada de Modelos (Models) 📦

- Simples classes com os campos de dados. <!-- .element: class="fragment" -->
- Fábricas `fromJson` e `toJson`. <!-- .element: class="fragment" -->

---

## 4. A Camada de Serviços (Services) 📡

- Onde o `http.get` e o `db.query` vivem. <!-- .element: class="fragment" -->
- Devolvem dados prontos para o app. <!-- .element: class="fragment" -->

---

## 5. A Camada de Estado (Providers) 🔄

- O elo entre o Serviço e a Tela. <!-- .element: class="fragment" -->
- Chama o serviço e avisa a tela quem mudou. <!-- .element: class="fragment" -->

---

## 6. O Princípio DRY (Don't Repeat Yourself) ♻️

- Se você copiou e colou, algo está errado. <!-- .element: class="fragment" -->
- Crie widgets reutilizáveis e funções genéricas. <!-- .element: class="fragment" -->

---

## 7. Componentização: Widgets Customizados 🧩

- Extraia pequenos pedaços da tela. <!-- .element: class="fragment" -->
- Um botão que você usa em 3 telas deve ser um arquivo único. <!-- .element: class="fragment" -->

---

## 8. Naming Conventions (Nomenclatura) 📛

- Snake_case para arquivos. <!-- .element: class="fragment" -->
- CamelCase para classes. <!-- .element: class="fragment" -->
- Verbos claros: `getUsuarios()`, `saveNota()`. <!-- .element: class="fragment" -->

---

## 9. O que é um Linter? 📏

- Um fiscal de código em tempo real. <!-- .element: class="fragment" -->
- Avisa se falta um `const`, se a variável não é usada, etc. <!-- .element: class="fragment" -->

---

## 10. Documentação (DartDoc) 📝

- Use `///` para explicar o porquê de uma função complexa existir. <!-- .element: class="fragment" -->

---

## 11. Git Flow Básico 🌿

- Trabalhar em branches (ramos). <!-- .element: class="fragment" -->
- Commits com mensagens claras. <!-- .element: class="fragment" -->

---

## 12. Performance: Evitando Rebuilds ⚡

- Mantenha os métodos `build` o mais limpos possível. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Organização é investimento de longo prazo. <!-- .element: class="fragment" -->
- Camadas protegem seu código. <!-- .element: class="fragment" -->
- Seja preguiçoso: escreva componentes reutilizáveis. <!-- .element: class="fragment" -->

---

## Próxima Aula: Publicando para Android 🤖

- Build de produção. <!-- .element: class="fragment" -->
- Ícones e Versões. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Código limpo não é sobre perfeccionismo, é sobre economia de tempo."