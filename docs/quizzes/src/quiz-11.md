# Quiz 11 - Persistência de Dados 💾

1. Qual pacote é o mais indicado para salvar pequenas preferências (ex: tema, login persistente)?
    - [ ] sqflite
    - [x] shared_preferences
    - [ ] file_picker
    - [ ] path_provider
    *Explicação: `SharedPreferences` é ideal para dados simples do tipo "chave-valor".*

2. A persistência com `SharedPreferences` é síncrona ou assíncrona?
    - [ ] Síncrona.
    - [x] Assíncrona (usa `Future`).
    - [ ] Depende do sistema operacional.
    - [ ] Não existe no Flutter.
    *Explicação: Como envolve escrita em disco, as operações são assíncronas para não travar a UI.*

3. Qual o banco de dados SQL oficial para uso local no Flutter?
    - [ ] MySQL
    - [ ] PostgreSQL
    - [x] SQLite (via pacote sqflite)
    - [ ] MongoDB
    *Explicação: O SQLite é um banco de dados relacional leve que mora dentro do arquivo do aplicativo.*

4. O que significa a sigla CRUD?
    - [ ] Create, Run, Update, Debug.
    - [x] Create, Read, Update, Delete.
    - [ ] Code, Read, Undo, Done.
    - [ ] Clear, Reset, Upload, Destroy.
    *Explicação: São as quatro operações básicas de qualquer banco de dados.*

5. Para que serve o comando `CREATE TABLE` no SQLite?
    - [ ] Para deletar tudo.
    - [x] Para definir a estrutura (colunas e tipos) de uma nova tabela.
    - [ ] Para inserir um novo usuário.
    - [ ] Para mudar a cor do app.
    *Explicação: Antes de salvar dados, precisamos definir como a "gaveta" (tabela) deve ser.*

6. Qual o papel da Primary Key (Chave Primária) em um banco de dados?
    - [ ] Abrir o aplicativo.
    - [x] Identificar de forma única e exclusiva cada registro na tabela (ex: um ID).
    - [ ] Ser a senha do banco.
    - [ ] Guardar fotos.
    *Explicação: A chave primária garante que nunca existam dois registros idênticos.*

7. Como inserimos um novo dado no SQLite?
    - [ ] db.add(...)
    - [x] db.insert('nome_tabela', dados_map)
    - [ ] db.save(...)
    - [ ] db.new(...)
    *Explicação: O método `insert` recebe o nome da tabela e um `Map` com os valores.*

8. O que acontece com os dados salvos em SQLite quando o aplicativo é fechado?
    - [ ] Eles são apagados.
    - [ ] Eles são enviados para o Google.
    - [x] Eles permanecem guardados permanentemente no disco do celular.
    - [ ] O celular explode.
    *Explicação: Persistência significa que os dados sobrevivem ao fechamento ou reinicialização do app.*

9. Qual pacote usamos para encontrar o caminho correto das pastas do sistema (como /Documents)?
    - [ ] url_launcher
    - [ ] google_fonts
    - [x] path_provider
    - [ ] flutter_svg
    *Explicação: O `path_provider` garante que o app encontre o local seguro para salvar arquivos em cada SO.*

10. Quando devemos preferir um Banco de Dados a um arquivo SharedPreferences?
    - [ ] Quando quisermos mudar a cor do botão.
    - [x] Quando tivermos grandes volumes de dados relacionados (como uma lista de centenas de produtos).
    - [ ] Nunca, SharedPreferences é sempre melhor.
    - [ ] Quando o app for apenas para Web.
    *Explicação: Bancos de dados relacionais permitem buscas complexas e filtros em grandes massas de dados.*
