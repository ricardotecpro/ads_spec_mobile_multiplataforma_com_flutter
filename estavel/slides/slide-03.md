# Aula 03 - Estrutura de um Projeto Flutter 🏗️
## Anatomia de um Aplicativo Profissional

---

## Agenda de Hoje 📅

1. Visão Geral das Pastas <!-- .element: class="fragment" -->
2. O Coração do Projeto: lib/ <!-- .element: class="fragment" -->
3. pubspec.yaml: Dependências e Assets <!-- .element: class="fragment" -->
4. Entry Point: main() <!-- .element: class="fragment" -->
5. Configurações de Plataforma <!-- .element: class="fragment" -->

---

## 1. Criando o Projeto 🚀

```termynal
$ flutter create meu_vovo_app
```
- O Flutter gera dezenas de arquivos prontos para você. <!-- .element: class="fragment" -->

---

## 2. A Pasta Principal: lib/ 📂

- Onde o seu código Dart vive. <!-- .element: class="fragment" -->
- `main.dart`: O primeiro arquivo a ser lido. <!-- .element: class="fragment" -->

---

## 3. Pastas de Plataforma 🤖🍎🌐

- `android/`: Projetos Gradle. <!-- .element: class="fragment" -->
- `ios/`: Projetos Xcode. <!-- .element: class="fragment" -->
- `web/`: index.html e manifest. <!-- .element: class="fragment" -->

---

## 4. pubspec.yaml: O Manifesto 📝

- Nome e Versão do App. <!-- .element: class="fragment" -->
- Dependências (Pacotes Externos). <!-- .element: class="fragment" -->
- Registro de Imagens e Fontes. <!-- .element: class="fragment" -->

---

## 5. Gerenciando dependências 📦

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.1.0
```
- Comando mágico: `flutter pub get`. <!-- .element: class="fragment" -->

---

## 6. O Ponto de Partida 🏁

```dart
void main() {
  runApp(const MyApp());
}
```
- `main()` inicia o Dart. <!-- .element: class="fragment" -->
- `runApp()` inicia o Flutter. <!-- .element: class="fragment" -->

---

## 7. MaterialApp: O Envelope ✉️

- Configura o tema do app. <!-- .element: class="fragment" -->
- Gerencia a navegação básica. <!-- .element: class="fragment" -->
- Aplica o vocabulário visual do Google. <!-- .element: class="fragment" -->

---

## 8. Scaffold: O Esqueleto 🦴

- `appBar`: Parte superior. <!-- .element: class="fragment" -->
- `body`: Conteúdo principal. <!-- .element: class="fragment" -->
- `floatingActionButton`: Botão de ação. <!-- .element: class="fragment" -->

---

## 9. Organização Profissional 📂

- `models/`: Dados <!-- .element: class="fragment" -->
- `views/`: Telas <!-- .element: class="fragment" -->
- `widgets/`: Componentes reutilizáveis <!-- .element: class="fragment" -->

---

## 10. Pasta test/ 🧪

- Onde criamos os testes automatizados. <!-- .element: class="fragment" -->
- Garante que mudanças no código não quebrem o app. <!-- .element: class="fragment" -->

---

## 11. Diferença entre Android e iOS no Projeto ⚖️

- Diferentes formas de lidar com ícones e permissões. <!-- .element: class="fragment" -->
- Localizados nas pastas `android` e `ios`. <!-- .element: class="fragment" -->

---

## 12. O arquivo analysis_options.yaml 🩺

- Define regras de "estilo" de código (Linters). <!-- .element: class="fragment" -->
- Ajuda a manter o código limpo e padronizado. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- `lib` é o seu campo de trabalho. <!-- .element: class="fragment" -->
- `pubspec` é seu cesto de utilidades. <!-- .element: class="fragment" -->
- `main()` dá o comando de partida. <!-- .element: class="fragment" -->

---

## Próxima Aula: Widgets Básicos 🧱

- Stateless vs Stateful. <!-- .element: class="fragment" -->
- Criando a primeira interface real. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Uma boa estrutura de pastas hoje economiza horas de debug amanhã."