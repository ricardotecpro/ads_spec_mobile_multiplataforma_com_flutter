# Aula 03 - Estrutura de um Projeto Flutter 🏗️
## Anatomia de um Aplicativo Profissional

---

## Agenda de Hoje 📅

1. Visão Geral das Pastas { .fragment }
2. O Coração do Projeto: lib/ { .fragment }
3. pubspec.yaml: Dependências e Assets { .fragment }
4. Entry Point: main() { .fragment }
5. Configurações de Plataforma { .fragment }

---

## 1. Criando o Projeto 🚀

```termynal
$ flutter create meu_vovo_app
```
- O Flutter gera dezenas de arquivos prontos para você. { .fragment }

---

## 2. A Pasta Principal: lib/ 📂

- Onde o seu código Dart vive. { .fragment }
- `main.dart`: O primeiro arquivo a ser lido. { .fragment }

---

## 3. Pastas de Plataforma 🤖🍎🌐

- `android/`: Projetos Gradle. { .fragment }
- `ios/`: Projetos Xcode. { .fragment }
- `web/`: index.html e manifest. { .fragment }

---

## 4. pubspec.yaml: O Manifesto 📝

- Nome e Versão do App. { .fragment }
- Dependências (Pacotes Externos). { .fragment }
- Registro de Imagens e Fontes. { .fragment }

---

## 5. Gerenciando dependências 📦

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.1.0
```
- Comando mágico: `flutter pub get`. { .fragment }

---

## 6. O Ponto de Partida 🏁

```dart
void main() {
  runApp(const MyApp());
}
```
- `main()` inicia o Dart. { .fragment }
- `runApp()` inicia o Flutter. { .fragment }

---

## 7. MaterialApp: O Envelope ✉️

- Configura o tema do app. { .fragment }
- Gerencia a navegação básica. { .fragment }
- Aplica o vocabulário visual do Google. { .fragment }

---

## 8. Scaffold: O Esqueleto 🦴

- `appBar`: Parte superior. { .fragment }
- `body`: Conteúdo principal. { .fragment }
- `floatingActionButton`: Botão de ação. { .fragment }

---

## 9. Organização Profissional 📂

- `models/`: Dados { .fragment }
- `views/`: Telas { .fragment }
- `widgets/`: Componentes reutilizáveis { .fragment }

---

## 10. Pasta test/ 🧪

- Onde criamos os testes automatizados. { .fragment }
- Garante que mudanças no código não quebrem o app. { .fragment }

---

## 11. Diferença entre Android e iOS no Projeto ⚖️

- Diferentes formas de lidar com ícones e permissões. { .fragment }
- Localizados nas pastas `android` e `ios`. { .fragment }

---

## 12. O arquivo analysis_options.yaml 🩺

- Define regras de "estilo" de código (Linters). { .fragment }
- Ajuda a manter o código limpo e padronizado. { .fragment }

---

## Resumo da Aula ✅

- `lib` é o seu campo de trabalho. { .fragment }
- `pubspec` é seu cesto de utilidades. { .fragment }
- `main()` dá o comando de partida. { .fragment }

---

## Próxima Aula: Widgets Básicos 🧱

- Stateless vs Stateful. { .fragment }
- Criando a primeira interface real. { .fragment }

---

## Dúvidas? 🤔

> "Uma boa estrutura de pastas hoje economiza horas de debug amanhã."