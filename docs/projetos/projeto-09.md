# Projeto 09 - Lista de Desejos 🔄

### 🎯 Objetivo
Aplicar o gerenciamento de estado global usando o pacote `Provider`.

---

### 📝 Descrição
Crie um aplicativo onde o usuário pode visualizar uma lista de produtos e "favoritar" aqueles que deseja. O estado do coração deve ser compartilhado entre diferentes widgets.

### 🛠️ Requisitos
1.  Instalação e configuração do pacote `Provider`.
2.  Criação de um `ChangeNotifier` para gerenciar a lista de favoritos.
3.  Uso de `context.watch()` para exibir o contador de favoritos.
4.  Uso de `context.read()` para adicionar/remover itens.

### 💡 Dica
Lembre-se de envolver seu `MaterialApp` com o `ChangeNotifierProvider` no arquivo `main.dart`.