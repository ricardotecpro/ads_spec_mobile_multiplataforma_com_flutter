# Quiz 02 - Linguagem Dart para Iniciantes 🎯

1. O que é o Dart?
    - [ ] Um framework para CSS.
    - [x] Uma linguagem de programação de tipagem forte criada pelo Google.
    - [ ] O nome do motor gráfico do Flutter.
    - [ ] Uma ferramenta de design para prototipagem.
    *Explicação: Dart é a linguagem base do Flutter, focada em performance e UI.*

2. Como declaramos uma variável com inferência de tipo no Dart?
    - [ ] int x = 10;
    - [ ] string nome = "Oi";
    - [x] var valor = 50;
    - [ ] dynamic x = 10;
    *Explicação: O `var` permite que o Dart descubra o tipo da variável automaticamente pelo valor atribuído.*

3. O que é o "Null Safety" no Dart?
    - [ ] Uma forma de apagar todas as variáveis nulas.
    - [x] Um recurso que evita erros de acesso a referências nulas em tempo de compilação.
    - [ ] Um sistema de segurança contra vírus.
    - [ ] Um modo de converter nulos em zeros.
    *Explicação: O Null Safety obriga o programador a tratar valores nulos explicitamente, evitando o famoso "null pointer exception".*

4. Qual operador usamos para permitir que uma variável aceite valores nulos?
    - [ ] !
    - [x] ?
    - [ ] ??
    - [ ] .
    *Explicação: O `?` após o tipo (ex: `String?`) indica que aquela variável pode receber `null`.*

5. Como se define uma função que não retorna nenhum valor?
    - [ ] def
    - [ ] function
    - [ ] empty
    - [x] void
    *Explicação: `void` é a palavra-chave para funções que executam uma tarefa sem devolver um resultado.*

6. Qual a saída do código: `var x = "10"; print(x.runtimeType);`?
    - [ ] int
    - [x] String
    - [ ] dynamic
    - [ ] double
    *Explicação: Como o valor está entre aspas, o Dart infere que o tipo é String.*

7. Para que serve o operador `??` no Dart?
    - [ ] Comparar se dois valores são nulos.
    - [x] Fornecer um valor padrão caso o operando da esquerda seja nulo.
    - [ ] Forçar uma variável a ser nula.
    - [ ] Multiplicar dois valores.
    *Explicação: Ex: `nome ?? "Anônimo"` retorna "Anônimo" se `nome` for nulo.*

8. Qual o tipo de dado correto para números decimais (ex: 3.14)?
    - [ ] int
    - [ ] float
    - [x] double
    - [ ] decimal
    *Explicação: No Dart, números de ponto flutuante são do tipo `double`.*

9. O que faz o comando `final` antes de uma variável?
    - [ ] Torna a variável global.
    - [x] Impede que o valor da variável seja alterado após a primeira atribuição.
    - [ ] Deleta a variável após o uso.
    - [ ] Faz a variável ser nula.
    *Explicação: `final` define uma constante que só pode ser definida uma única vez.*

10. Como realizamos a interpolação de strings no Dart?
    - [ ] "Olá " + nome
    - [x] "Olá $nome"
    - [ ] "Olá {nome}"
    - [ ] "Olá #nome"
    *Explicação: O símbolo `$` permite inserir o valor de uma variável diretamente dentro de uma String.*
