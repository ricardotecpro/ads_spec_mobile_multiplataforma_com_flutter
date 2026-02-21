# Quiz 12 - Organização Profissional do Projeto 🏛️

1. Por que a organização de pastas é importante em um projeto profissional?
    - [ ] Para o computador não travar.
    - [ ] Para o aplicativo ser mais caro.
    - [x] Para facilitar a manutenção, escalabilidade e o trabalho em equipe.
    - [ ] Não é importante, basta tudo estar na pasta 'lib/'.
    *Explicação: Um projeto bagunçado se torna impossível de atualizar rapidamente sem criar novos bugs.*

2. No padrão de camadas, o que a camada "Model" representa?
    - [ ] Os desenhos da interface.
    - [x] As classes que definem a estrutura dos dados do sistema.
    - [ ] As chamadas de internet.
    - [ ] O código do banco de dados.
    *Explicação: O Model é o "molde" dos seus objetos (ex: uma classe `Usuario`).*

3. Qual a função da camada "Service"?
    - [ ] Desenhar botões.
    - [x] Lidar com lógica Pure-Data e comunicação externa (API/Banco).
    - [ ] Definir o tema do app.
    - [ ] Guardar as senhas do usuário.
    *Explicação: Services isolam a complexidade de rede da interface do usuário.*

4. O que significa o princípio DRY (Don't Repeat Yourself)?
    - [ ] Não beba água enquanto programa.
    - [ ] Escreva o código o mais rápido possível.
    - [x] Evite a duplicação de lógica criando código reutilizável.
    - [ ] Comente todas as linhas de código.
    *Explicação: Código repetido significa que se você achar um erro, terá que corrigir em vários lugares.*

5. O que é um "Widget Customizado"?
    - [ ] Um widget que você comprou na internet.
    - [x] Um novo widget criado por você ao extrair partes repetidas da interface.
    - [ ] Um widget que só roda no iPhone.
    - [ ] O widget Scaffold.
    *Explicação: Criar seus próprios widgets (como um `MeuBotaoPadrao`) mantém a UI limpa e consistente.*

6. Qual a vantagem da "Separação de Preocupações" (Separation of Concerns)?
    - [ ] O app fica com menos pastas.
    - [x] Cada parte do código faz apenas o que é sua responsabilidade, facilitando testes e correções.
    - [ ] As fotos ficam em alta definição.
    - [ ] Não precisa usar Git.
    *Explicação: Se o erro for na tela, você sabe que o problema está na View, não no Service.*

7. Na Clean Architecture, quem deve conhecer quem?
    - [ ] O Banco de Dados deve conhecer a Tela.
    - [x] A Camada Externa (UI) depende das camadas internas (Lógica), nunca o contrário.
    - [ ] Ninguém conhece ninguém.
    - [ ] Depende do humor do desenvolvedor.
    *Explicação: A lógica de negócio deve ser independente da interface para que você possa trocar a UI sem quebrar o sistema.*

8. O que é um "Singleton"?
    - [ ] Um programador que trabalha sozinho.
    - [x] Um padrão de projeto que garante que uma classe tenha apenas uma única instância em todo o app.
    - [ ] Uma variável que só aceita números 1.
    - [ ] O nome do banco de dados.
    *Explicação: Útil para classes de Configuração ou instâncias de Banco de Dados.*

9. Para que serve o arquivo `.gitignore`?
    - [ ] Para esconder seu código do Google.
    - [x] Para evitar que arquivos desnecessários ou sensíveis (como chaves de acesso) sejam enviados ao servidor de controle de versão.
    - [ ] Para deletar o projeto.
    - [ ] Para mudar a cor das pastas.
    *Explicação: Ele mantém o repositório limpo salvando apenas o código fonte real.*

10. Como se chama a prática de melhorar o código sem mudar seu comportamento externo?
    - [ ] Coding.
    - [ ] Debugging.
    - [x] Refatoração.
    - [ ] Compilação.
    *Explicação: Refatorar é "limpar a casa", tornando o código mais legível e eficiente.*
