# Exercícios - Aula 11: Persistência de Dados 💾

### 🟢 Básicos (Fixação)

1. **Armazenamento**: Qual pacote você escolheria para salvar se o usuário prefere o app em "Modo Escuro" ou "Modo Claro"? Justifique.
2. **SQLite**: O SQLite é considerado um banco de dados relacional ou não-relacional (NoSQL)?

### 🟡 Intermediários (Aplicação)

3. **CRUD**: Escreva o comando SQL necessário para criar uma tabela chamada `tarefas` com as colunas `id` (inteiro), `titulo` (texto) e `concluida` (inteiro 0 ou 1).
4. **Camadas**: Por que não é boa prática abrir a conexão com o banco de dados diretamente dentro do método `build` da sua tela?

### 🔴 Desafio (Pesquisa/Prática)

5. **Sincronização**: Imagine um app que funciona offline mas precisa enviar os dados para a nuvem quando a internet volta. Pesquise e explique brevemente como você organizaria esse fluxo de dados.