# Aula 11 - Persistência de Dados 💾
## Guardando Informações no Dispositivo

---

## Agenda de Hoje 📅

1. Tipos de Armazenamento { .fragment }
2. SharedPreferences (Simples) { .fragment }
3. SQLite (Complexo/Relacional) { .fragment }
4. O Pacote sqflite { .fragment }
5. CRUD na Prática { .fragment }

---

## 1. Por que persistir? 🤔

- O usuário não quer digitar tudo de novo. { .fragment }
- O app deve funcionar (parcialmente) sem internet. { .fragment }

---

## 2. SharedPreferences 📂

- Chave-Valor (`tema: escuro`). { .fragment }
- Ideal para: Strings, booleans, ints pequenos. { .fragment }
- Extremamente rápido de implementar. { .fragment }

---

## 3. SQLite: O Banco Gigante 🏛️

- Banco de dados real dentro do celular. { .fragment }
- Tabelas, Colunas e SQL. { .fragment }
- Ideal para: Centenas ou milhares de itens relacionados. { .fragment }

---

## 4. O Pacote sqflite 📦

- Driver oficial para SQLite no Flutter. { .fragment }
- Gerencia versões do banco (Migrations). { .fragment }

---

## 5. CRUD: As 4 Operações 🛠️

- **C**reate: Inserir. { .fragment }
- **R**ead: Listar/Buscar. { .fragment }
- **U**pdate: Atualizar. { .fragment }
- **D**elete: Apagar. { .fragment }

---

## 6. O Padrão Singleton para o Banco 🔑

- Garantir que apenas uma "conexão" exista para o app inteiro. { .fragment }

---

## 7. Escrevendo SQL no Dart ✍️

```sql
SELECT * FROM tarefas WHERE concluida = 0;
```

---

## 8. Abstração: Mapas e Modelos 🗺️

- O SQLite devolve `List<Map>`. { .fragment }
- Nós transformamos em objetos Dart (`Usuario`, `Tarefa`). { .fragment }

---

## 9. Performance: Escrita Assíncrona ⚡

- Nunca grave no banco na Thread Principal. { .fragment }
- O Flutter/Dart já faz isso via `await` automaticamente. { .fragment }

---

## 10. Path Provider 📍

- Onde os arquivos moram? { .fragment }
- O iOS e Android têm pastas protegidas para o banco. { .fragment }

---

## 11. Segurança: Criptografia? 🔒

- Bancos padrão não são criptografados. { .fragment }
- Para dados sensíveis, use `SQLCipher`. { .fragment }

---

## 12. Alternativa NoSQL: Hive / Isar 🐝

- Opções modernas e extremamente rápidas que não usam SQL. { .fragment }

---

## Resumo da Aula ✅

- Persistência traz utilidade ao app. { .fragment }
- SharedPrefs para o básico. { .fragment }
- SQLite para o profissional. { .fragment }

---

## Próxima Aula: Organização Profissional 🏛️

- Arquitetura de Camadas. { .fragment }
- Deixando o código pronto para grandes times. { .fragment }

---

## Dúvidas? 🤔

> "Dados são a alma do seu aplicativo. Cuide bem de onde você os guarda."