# Quiz 11 - Persistência de Dados 💾

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual pacote é o mais indicado para salvar pequenas preferências (ex: tema, login persistente)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `SharedPreferences` é ideal para dados simples do tipo "chave-valor".">sqflite</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `SharedPreferences` é ideal para dados simples do tipo "chave-valor".">shared_preferences</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `SharedPreferences` é ideal para dados simples do tipo "chave-valor".">file_picker</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `SharedPreferences` é ideal para dados simples do tipo "chave-valor".">path_provider</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. A persistência com `SharedPreferences` é síncrona ou assíncrona?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como envolve escrita em disco, as operações são assíncronas para não travar a UI.">Síncrona.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Como envolve escrita em disco, as operações são assíncronas para não travar a UI.">Assíncrona (usa `Future`).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como envolve escrita em disco, as operações são assíncronas para não travar a UI.">Depende do sistema operacional.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como envolve escrita em disco, as operações são assíncronas para não travar a UI.">Não existe no Flutter.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual o banco de dados SQL oficial para uso local no Flutter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SQLite é um banco de dados relacional leve que mora dentro do arquivo do aplicativo.">MySQL</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SQLite é um banco de dados relacional leve que mora dentro do arquivo do aplicativo.">PostgreSQL</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O SQLite é um banco de dados relacional leve que mora dentro do arquivo do aplicativo.">SQLite (via pacote sqflite)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SQLite é um banco de dados relacional leve que mora dentro do arquivo do aplicativo.">MongoDB</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que significa a sigla CRUD?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. São as quatro operações básicas de qualquer banco de dados.">Create, Run, Update, Debug.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! São as quatro operações básicas de qualquer banco de dados.">Create, Read, Update, Delete.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. São as quatro operações básicas de qualquer banco de dados.">Code, Read, Undo, Done.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. São as quatro operações básicas de qualquer banco de dados.">Clear, Reset, Upload, Destroy.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve o comando `CREATE TABLE` no SQLite?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Antes de salvar dados, precisamos definir como a "gaveta" (tabela) deve ser.">Para deletar tudo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Antes de salvar dados, precisamos definir como a "gaveta" (tabela) deve ser.">Para definir a estrutura (colunas e tipos) de uma nova tabela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Antes de salvar dados, precisamos definir como a "gaveta" (tabela) deve ser.">Para inserir um novo usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Antes de salvar dados, precisamos definir como a "gaveta" (tabela) deve ser.">Para mudar a cor do app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o papel da Primary Key (Chave Primária) em um banco de dados?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A chave primária garante que nunca existam dois registros idênticos.">Abrir o aplicativo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A chave primária garante que nunca existam dois registros idênticos.">Identificar de forma única e exclusiva cada registro na tabela (ex: um ID).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A chave primária garante que nunca existam dois registros idênticos.">Ser a senha do banco.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A chave primária garante que nunca existam dois registros idênticos.">Guardar fotos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como inserimos um novo dado no SQLite?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `insert` recebe o nome da tabela e um `Map` com os valores.">db.add(...)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O método `insert` recebe o nome da tabela e um `Map` com os valores.">db.insert('nome_tabela', dados_map)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `insert` recebe o nome da tabela e um `Map` com os valores.">db.save(...)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `insert` recebe o nome da tabela e um `Map` com os valores.">db.new(...)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que acontece com os dados salvos em SQLite quando o aplicativo é fechado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Persistência significa que os dados sobrevivem ao fechamento ou reinicialização do app.">Eles são apagados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Persistência significa que os dados sobrevivem ao fechamento ou reinicialização do app.">Eles são enviados para o Google.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Persistência significa que os dados sobrevivem ao fechamento ou reinicialização do app.">Eles permanecem guardados permanentemente no disco do celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Persistência significa que os dados sobrevivem ao fechamento ou reinicialização do app.">O celular explode.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual pacote usamos para encontrar o caminho correto das pastas do sistema (como /Documents)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `path_provider` garante que o app encontre o local seguro para salvar arquivos em cada SO.">url_launcher</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `path_provider` garante que o app encontre o local seguro para salvar arquivos em cada SO.">google_fonts</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `path_provider` garante que o app encontre o local seguro para salvar arquivos em cada SO.">path_provider</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `path_provider` garante que o app encontre o local seguro para salvar arquivos em cada SO.">flutter_svg</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Quando devemos preferir um Banco de Dados a um arquivo SharedPreferences?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Bancos de dados relacionais permitem buscas complexas e filtros em grandes massas de dados.">Quando quisermos mudar a cor do botão.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Bancos de dados relacionais permitem buscas complexas e filtros em grandes massas de dados.">Quando tivermos grandes volumes de dados relacionados (como uma lista de centenas de produtos).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Bancos de dados relacionais permitem buscas complexas e filtros em grandes massas de dados.">Nunca, SharedPreferences é sempre melhor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Bancos de dados relacionais permitem buscas complexas e filtros em grandes massas de dados.">Quando o app for apenas para Web.</div>
  <div class="quiz-feedback"></div>
</div>
