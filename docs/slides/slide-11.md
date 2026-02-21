# Aula 11 - Persistência de Dados 💾
## Guardando Informações no Dispositivo

---

## Agenda de Hoje 📅

1. Tipos de Armazenamento <!-- .element: class="fragment" -->
2. SharedPreferences (Simples) <!-- .element: class="fragment" -->
3. SQLite (Complexo/Relacional) <!-- .element: class="fragment" -->
4. O Pacote sqflite <!-- .element: class="fragment" -->
5. CRUD na Prática <!-- .element: class="fragment" -->

---

## 1. Por que persistir? 🤔

- O usuário não quer digitar tudo de novo. <!-- .element: class="fragment" -->
- O app deve funcionar (parcialmente) sem internet. <!-- .element: class="fragment" -->

---

## 2. SharedPreferences 📂

- Chave-Valor (`tema: escuro`). <!-- .element: class="fragment" -->
- Ideal para: Strings, booleans, ints pequenos. <!-- .element: class="fragment" -->
- Extremamente rápido de implementar. <!-- .element: class="fragment" -->

---

## 3. SQLite: O Banco Gigante 🏛️

- Banco de dados real dentro do celular. <!-- .element: class="fragment" -->
- Tabelas, Colunas e SQL. <!-- .element: class="fragment" -->
- Ideal para: Centenas ou milhares de itens relacionados. <!-- .element: class="fragment" -->

---

## 4. O Pacote sqflite 📦

- Driver oficial para SQLite no Flutter. <!-- .element: class="fragment" -->
- Gerencia versões do banco (Migrations). <!-- .element: class="fragment" -->

---

## 5. CRUD: As 4 Operações 🛠️

- **C**reate: Inserir. <!-- .element: class="fragment" -->
- **R**ead: Listar/Buscar. <!-- .element: class="fragment" -->
- **U**pdate: Atualizar. <!-- .element: class="fragment" -->
- **D**elete: Apagar. <!-- .element: class="fragment" -->

---

## 6. O Padrão Singleton para o Banco 🔑

- Garantir que apenas uma "conexão" exista para o app inteiro. <!-- .element: class="fragment" -->

---

## 7. Escrevendo SQL no Dart ✍️

```sql
SELECT * FROM tarefas WHERE concluida = 0;
```

---

## 8. Abstração: Mapas e Modelos 🗺️

- O SQLite devolve `List<Map>`. <!-- .element: class="fragment" -->
- Nós transformamos em objetos Dart (`Usuario`, `Tarefa`). <!-- .element: class="fragment" -->

---

## 9. Performance: Escrita Assíncrona ⚡

- Nunca grave no banco na Thread Principal. <!-- .element: class="fragment" -->
- O Flutter/Dart já faz isso via `await` automaticamente. <!-- .element: class="fragment" -->

---

## 10. Path Provider 📍

- Onde os arquivos moram? <!-- .element: class="fragment" -->
- O iOS e Android têm pastas protegidas para o banco. <!-- .element: class="fragment" -->

---

## 11. Segurança: Criptografia? 🔒

- Bancos padrão não são criptografados. <!-- .element: class="fragment" -->
- Para dados sensíveis, use `SQLCipher`. <!-- .element: class="fragment" -->

---

## 12. Alternativa NoSQL: Hive / Isar 🐝

- Opções modernas e extremamente rápidas que não usam SQL. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Persistência traz utilidade ao app. <!-- .element: class="fragment" -->
- SharedPrefs para o básico. <!-- .element: class="fragment" -->
- SQLite para o profissional. <!-- .element: class="fragment" -->

---

## Próxima Aula: Organização Profissional 🏛️

- Arquitetura de Camadas. <!-- .element: class="fragment" -->
- Deixando o código pronto para grandes times. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Dados são a alma do seu aplicativo. Cuide bem de onde você os guarda."