# Aula 01 - Introdução ao Desenvolvimento Multiplataforma 🌍
## Um Código, Todas as Telas

---

## Agenda de Hoje 📅

1. O que é Multiplataforma? { .fragment }
2. Nativo vs Híbrido vs Flutter { .fragment }
3. Por que Flutter? { .fragment }
4. Ecossistema e Renderização { .fragment }
5. Ferramentas Necesárias { .fragment }
6. Primeiro Projeto { .fragment }

---

## 1. O Desafio Mobile 📱

- Antes: Equipes separadas para Android (Java) e iOS (Swift). { .fragment }
- Problema: Custo dobrado e manutenção difícil. { .fragment }
- Solução: Frameworks Multiplataforma. { .fragment }

---

## 2. Abordagem Nativa 🍎🤖

- Performance máxima. { .fragment }
- Acesso total ao hardware. { .fragment }
- Duas bases de código. { .fragment }

---

## 3. Abordagem Híbrida (WebView) 🌐

- HTML/CSS/JS dentro de um navegador. { .fragment }
- Lento e com visual "não-nativo". { .fragment }
- Ex: PhoneGap, Cordova. { .fragment }

---

## 4. O Diferencial do Flutter 🦄

- Desenha cada pixel na tela (Canvas). { .fragment }
- Não usa WebView nem OEM Widgets nativos. { .fragment }
- Alta performance (60/120 fps). { .fragment }

---

## 5. Estrutura de Renderização 📊

```mermaid
graph TD
    A[App Flutter] --> B[Framework - Dart]
    B --> C[Engine - C++]
    C --> D[Skia/Impeller - Graphics]
    D --> E[Plataforma - Android/iOS/Web]
```

---

## 6. Por que Dart? 🎯

- Compilação AOT (Ahead-of-Time). { .fragment }
- Ciclo de desenvolvimento rápido (JIT). { .fragment }
- Otimizada para interfaces de usuário. { .fragment }

---

## 7. Hot Reload: Magia Pura ⚡

- Mudanças instantâneas no código. { .fragment }
- Mantém o estado do app. { .fragment }
- Produtividade multiplicada por 10. { .fragment }

---

## 8. Cinto de Utilidades 🛠️

- Flutter SDK { .fragment }
- Android Studio / VS Code { .fragment }
- Emuladores ou Celular Real { .fragment }

---

## 9. Flutter Doctor 🩺

- "O médico do seu ambiente". { .fragment }
- Mostra o que falta instalar. { .fragment }
- Garante que tudo está pronto para rodar. { .fragment }

---

## 10. Criando seu Primeiro App 🚀

```termynal
$ flutter create meu_app
$ cd meu_app
$ flutter run
```

---

## 11. Onde as Mágicas Acontecem? 📂

- Pasta `lib/`: Seu código mora aqui. { .fragment }
- Arquivo `main.dart`: O coração do app. { .fragment }

---

## 12. Plataformas Suportadas 🍏🤖🖥️🌐

- Android & iOS (Mobile) { .fragment }
- Web (HTML/Wasm) { .fragment }
- Windows, macOS, Linux (Desktop) { .fragment }

---

## 13. Flutter no Mercado 💼

- Usado por: Google, Alibaba, BMW, Nubank. { .fragment }
- Comunidade gigante e crescente. { .fragment }

---

## Resumo da Aula ✅

- Flutter = Alta Performance + Um Código. { .fragment }
- Dart = Linguagem produtiva. { .fragment }
- Hot Reload = Super poder. { .fragment }

---

## Próxima Aula: Linguagem Dart 🎯

- Variáveis, Funções e Lógica. { .fragment }
- Preparando para o código real. { .fragment }

---

## Dúvidas? 🤔

> "Escreva uma vez, execute em qualquer lugar."
