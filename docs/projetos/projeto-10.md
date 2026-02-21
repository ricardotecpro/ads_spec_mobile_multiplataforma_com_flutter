# Projeto 10 - Consulta de CEP 📡

### 🎯 Objetivo
Consumir dados de uma API externa e tratar processos assíncronos.

---

### 📝 Descrição
Desenvolva um buscador de endereços. O usuário digita o CEP e o aplicativo busca as informações (Rua, Bairro, Cidade) usando a API do ViaCEP.

### 🛠️ Requisitos
1.  Uso do pacote `http`.
2.  Chamada assíncrona (`async`/`await`) para a API.
3.  Tratamento de erro (caso o CEP não exista).
4.  Exibição de um `CircularProgressIndicator` durante a busca.

### 💡 Dica
A URL da API é: `https://viacep.com.br/ws/01001000/json/`. Substitua o número pelo valor digitado pelo usuário.