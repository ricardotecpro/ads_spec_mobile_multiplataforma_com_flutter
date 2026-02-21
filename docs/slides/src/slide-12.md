# Aula 12 - Organização Profissional 🏛️
## De Código para Engenharia

---

## Agenda de Hoje 📅

1. Por que Organizar? { .fragment }
2. Clean Architecture Simplificada { .fragment }
3. Models, Services e Providers { .fragment }
4. O Princípio DRY { .fragment }
5. Boas Práticas e Linter { .fragment }

---

## 1. O Código "Espaguete" 🍝

- Tudo no mesmo arquivo. { .fragment }
- Impossível de testar. { .fragment }
- Um bug corrigido gera três novos bugs. { .fragment }

---

## 2. Separação de Preocupações ✂️

- A Tela não deve saber como o Banco de Dados funciona. { .fragment }
- O Modelo não deve saber como ele é desenhado. { .fragment }

---

## 3. A Camada de Modelos (Models) 📦

- Simples classes com os campos de dados. { .fragment }
- Fábricas `fromJson` e `toJson`. { .fragment }

---

## 4. A Camada de Serviços (Services) 📡

- Onde o `http.get` e o `db.query` vivem. { .fragment }
- Devolvem dados prontos para o app. { .fragment }

---

## 5. A Camada de Estado (Providers) 🔄

- O elo entre o Serviço e a Tela. { .fragment }
- Chama o serviço e avisa a tela quem mudou. { .fragment }

---

## 6. O Princípio DRY (Don't Repeat Yourself) ♻️

- Se você copiou e colou, algo está errado. { .fragment }
- Crie widgets reutilizáveis e funções genéricas. { .fragment }

---

## 7. Componentização: Widgets Customizados 🧩

- Extraia pequenos pedaços da tela. { .fragment }
- Um botão que você usa em 3 telas deve ser um arquivo único. { .fragment }

---

## 8. Naming Conventions (Nomenclatura) 📛

- Snake_case para arquivos. { .fragment }
- CamelCase para classes. { .fragment }
- Verbos claros: `getUsuarios()`, `saveNota()`. { .fragment }

---

## 9. O que é um Linter? 📏

- Um fiscal de código em tempo real. { .fragment }
- Avisa se falta um `const`, se a variável não é usada, etc. { .fragment }

---

## 10. Documentação (DartDoc) 📝

- Use `///` para explicar o porquê de uma função complexa existir. { .fragment }

---

## 11. Git Flow Básico 🌿

- Trabalhar em branches (ramos). { .fragment }
- Commits com mensagens claras. { .fragment }

---

## 12. Performance: Evitando Rebuilds ⚡

- Mantenha os métodos `build` o mais limpos possível. { .fragment }

---

## Resumo da Aula ✅

- Organização é investimento de longo prazo. { .fragment }
- Camadas protegem seu código. { .fragment }
- Seja preguiçoso: escreva componentes reutilizáveis. { .fragment }

---

## Próxima Aula: Publicando para Android 🤖

- Build de produção. { .fragment }
- Ícones e Versões. { .fragment }

---

## Dúvidas? 🤔

> "Código limpo não é sobre perfeccionismo, é sobre economia de tempo."