# Aula 02 - Linguagem Dart para Iniciantes 🎯
## A Linguagem do Flutter

---

## Agenda de Hoje 📅

1. O que é Dart? <!-- .element: class="fragment" -->
2. Variáveis e Tipagem <!-- .element: class="fragment" -->
3. Null Safety <!-- .element: class="fragment" -->
4. Estruturas de Controle <!-- .element: class="fragment" -->
5. Funções <!-- .element: class="fragment" -->
6. Exercício Prático <!-- .element: class="fragment" -->

---

## 1. O que é Dart? 🤔

- Criada pelo Google em 2011. <!-- .element: class="fragment" -->
- Focada em desenvolvimento client-side. <!-- .element: class="fragment" -->
- Familiar a quem conhece Java ou JavaScript. <!-- .element: class="fragment" -->

---

## 2. Tudo é Objeto 📦

- Números, funções e null são objetos. <!-- .element: class="fragment" -->
- Herda de uma classe base `Object`. <!-- .element: class="fragment" -->

---

## 3. Variáveis e Tipos 🏷️

```dart
String nome = "Dart";
int idade = 12;
double pi = 3.1415;
bool isStable = true;
```

---

## 4. Inferência de Tipo (var) 🔍

- O Dart descobre o tipo para você. <!-- .element: class="fragment" -->
- `var linguagem = "Flutter";` -> O Dart sabe que é String. <!-- .element: class="fragment" -->

---

## 5. Constantes (final e const) 🔒

- `final`: Valor definido uma única vez (em tempo de execução). <!-- .element: class="fragment" -->
- `const`: Constante em tempo de compilação. <!-- .element: class="fragment" -->

---

## 6. Null Safety: O Fim dos Erros Nulos 🛡️

- Por padrão, variáveis não aceitam nulo. <!-- .element: class="fragment" -->
- Use `?` para permitir nulos: `String? nome;` <!-- .element: class="fragment" -->

---

## 7. Operadores de Null Safety ⚡

- `??`: Valor padrão se for nulo. <!-- .element: class="fragment" -->
- `!`: Forçar que o valor não é nulo. <!-- .element: class="fragment" -->
- `?.`: Acessar propriedade apenas se não for nulo. <!-- .element: class="fragment" -->

---

## 8. Estruturas de Decisão 🚦

```dart
if (nota >= 7) {
  print("Aprovado");
} else {
  print("Recuperação");
}
```

---

## 9. Laços de Repetição 🔄

```dart
for (var i = 1; i <= 5; i++) {
  print("Aula $i");
}
```

---

## 10. Funções 🛠️

```dart
void saudar(String nome) {
  print("Olá, $nome!");
}
```

---

## 11. Funções de Uma Linha (Arrow) ➡️

```dart
double dobro(double n) => n * 2;
```

---

## 12. Interpolação de Strings 🧵

```dart
var versao = 3.19;
print("Rodando Flutter na versao $versao");
```

---

## 13. Comentários no Código 📝

- `//` Linha única. <!-- .element: class="fragment" -->
- `/* ... */` Múltiplas linhas. <!-- .element: class="fragment" -->
- `///` Documentação. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Dart é poderosa e segura. <!-- .element: class="fragment" -->
- Null Safety protege nosso app. <!-- .element: class="fragment" -->
- Sintaxe amigável e moderna. <!-- .element: class="fragment" -->

---

## Próxima Aula: Estrutura do Projeto 🏗️

- Onde ficam os arquivos? <!-- .element: class="fragment" -->
- Configurando o pubspec.yaml. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Dart: Simples o suficiente para aprender rápido, poderosa o suficiente para grandes apps."
