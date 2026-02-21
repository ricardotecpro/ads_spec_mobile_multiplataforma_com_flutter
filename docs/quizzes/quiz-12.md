# Quiz 12 - Organização Profissional do Projeto 🏛️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Por que a organização de pastas é importante em um projeto profissional?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um projeto bagunçado se torna impossível de atualizar rapidamente sem criar novos bugs.">Para o computador não travar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um projeto bagunçado se torna impossível de atualizar rapidamente sem criar novos bugs.">Para o aplicativo ser mais caro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um projeto bagunçado se torna impossível de atualizar rapidamente sem criar novos bugs.">Para facilitar a manutenção, escalabilidade e o trabalho em equipe.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um projeto bagunçado se torna impossível de atualizar rapidamente sem criar novos bugs.">Não é importante, basta tudo estar na pasta 'lib/'.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. No padrão de camadas, o que a camada "Model" representa?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Model é o "molde" dos seus objetos (ex: uma classe `Usuario`).">Os desenhos da interface.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Model é o "molde" dos seus objetos (ex: uma classe `Usuario`).">As classes que definem a estrutura dos dados do sistema.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Model é o "molde" dos seus objetos (ex: uma classe `Usuario`).">As chamadas de internet.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Model é o "molde" dos seus objetos (ex: uma classe `Usuario`).">O código do banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a função da camada "Service"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Services isolam a complexidade de rede da interface do usuário.">Desenhar botões.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Services isolam a complexidade de rede da interface do usuário.">Lidar com lógica Pure-Data e comunicação externa (API/Banco).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Services isolam a complexidade de rede da interface do usuário.">Definir o tema do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Services isolam a complexidade de rede da interface do usuário.">Guardar as senhas do usuário.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que significa o princípio DRY (Don't Repeat Yourself)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Código repetido significa que se você achar um erro, terá que corrigir em vários lugares.">Não beba água enquanto programa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Código repetido significa que se você achar um erro, terá que corrigir em vários lugares.">Escreva o código o mais rápido possível.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Código repetido significa que se você achar um erro, terá que corrigir em vários lugares.">Evite a duplicação de lógica criando código reutilizável.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Código repetido significa que se você achar um erro, terá que corrigir em vários lugares.">Comente todas as linhas de código.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que é um "Widget Customizado"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Criar seus próprios widgets (como um `MeuBotaoPadrao`) mantém a UI limpa e consistente.">Um widget que você comprou na internet.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Criar seus próprios widgets (como um `MeuBotaoPadrao`) mantém a UI limpa e consistente.">Um novo widget criado por você ao extrair partes repetidas da interface.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Criar seus próprios widgets (como um `MeuBotaoPadrao`) mantém a UI limpa e consistente.">Um widget que só roda no iPhone.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Criar seus próprios widgets (como um `MeuBotaoPadrao`) mantém a UI limpa e consistente.">O widget Scaffold.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual a vantagem da "Separação de Preocupações" (Separation of Concerns)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se o erro for na tela, você sabe que o problema está na View, não no Service.">O app fica com menos pastas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Se o erro for na tela, você sabe que o problema está na View, não no Service.">Cada parte do código faz apenas o que é sua responsabilidade, facilitando testes e correções.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se o erro for na tela, você sabe que o problema está na View, não no Service.">As fotos ficam em alta definição.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se o erro for na tela, você sabe que o problema está na View, não no Service.">Não precisa usar Git.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Na Clean Architecture, quem deve conhecer quem?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A lógica de negócio deve ser independente da interface para que você possa trocar a UI sem quebrar o sistema.">O Banco de Dados deve conhecer a Tela.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A lógica de negócio deve ser independente da interface para que você possa trocar a UI sem quebrar o sistema.">A Camada Externa (UI) depende das camadas internas (Lógica), nunca o contrário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A lógica de negócio deve ser independente da interface para que você possa trocar a UI sem quebrar o sistema.">Ninguém conhece ninguém.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A lógica de negócio deve ser independente da interface para que você possa trocar a UI sem quebrar o sistema.">Depende do humor do desenvolvedor.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é um "Singleton"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para classes de Configuração ou instâncias de Banco de Dados.">Um programador que trabalha sozinho.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Útil para classes de Configuração ou instâncias de Banco de Dados.">Um padrão de projeto que garante que uma classe tenha apenas uma única instância em todo o app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para classes de Configuração ou instâncias de Banco de Dados.">Uma variável que só aceita números 1.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para classes de Configuração ou instâncias de Banco de Dados.">O nome do banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Para que serve o arquivo `.gitignore`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele mantém o repositório limpo salvando apenas o código fonte real.">Para esconder seu código do Google.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele mantém o repositório limpo salvando apenas o código fonte real.">Para evitar que arquivos desnecessários ou sensíveis (como chaves de acesso) sejam enviados ao servidor de controle de versão.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele mantém o repositório limpo salvando apenas o código fonte real.">Para deletar o projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele mantém o repositório limpo salvando apenas o código fonte real.">Para mudar a cor das pastas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como se chama a prática de melhorar o código sem mudar seu comportamento externo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Refatorar é "limpar a casa", tornando o código mais legível e eficiente.">Coding.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Refatorar é "limpar a casa", tornando o código mais legível e eficiente.">Debugging.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Refatorar é "limpar a casa", tornando o código mais legível e eficiente.">Refatoração.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Refatorar é "limpar a casa", tornando o código mais legível e eficiente.">Compilação.</div>
  <div class="quiz-feedback"></div>
</div>
