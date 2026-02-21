# Aula 15 - Aplicações Desktop 💻
## Flutter Nativo no PC

---

## Agenda de Hoje 📅

1. Status do Desktop no Flutter { .fragment }
2. Requisitos por SO { .fragment }
3. Interações Desktop (Mouse/Teclado) { .fragment }
4. Acesso ao Sistema de Arquivos { .fragment }
5. Compilação e Distribuição { .fragment }

---

## 1. Por que Desktop? 🖥️

- Performance nativa real (64 bits). { .fragment }
- Uso de todo o hardware do PC (GPU/Multi-core). { .fragment }
- Ferramentas internas e sistemas de gestão. { .fragment }

---

## 2. Requisitos Windows 🪟

- Visual Studio instalado. { .fragment }
- Workload de "C++ Desktop Development". { .fragment }

---

## 3. Requisitos macOS 🍎

- Xcode instalado e atualizado. { .fragment }

---

## 4. Requisitos Linux 🐧

- Bibliotecas GTK e Clang configuradas. { .fragment }

---

## 5. Menus e Atalhos de Teclado ⌨️

- Ctrl+S, Ctrl+Z. { .fragment }
- Barra de menus superior (File, Edit). { .fragment }
- Pacote `menubar` ou `shortcut_manager`. { .fragment }

---

## 6. Multi-Window (Múltiplas Janelas) 🪟🪟

- Recentemente adicionado ao Flutter de forma experimental/via pacotes. { .fragment }

---

## 7. Seleção de Arquivos 📂

- Abrir e salvar janelas nativas do sistema. { .fragment }
- Pacote `file_picker`. { .fragment }

---

## 8. Persistência Desktop 💾

- SQLite também funciona aqui! { .fragment }
- Arquivos JSON/Texto locais. { .fragment }

---

## 9. Rodando o Projeto 🚀

```termynal
$ flutter run -d windows
```

---

## 10. O Resultado: Executável Nativo 📦

- Nada de WebView. { .fragment }
- Nada de interpretador lento. { .fragment }
- Apenas código de máquina rodando direto no processador. { .fragment }

---

## 11. Bandeja do Sistema (System Tray) 📥

- Gerenciar o ícone do app perto do relógio. { .fragment }

---

## 12. Tamanho da Janela Inicial 📏

- Definir o tamanho padrão no código nativo (C++ ou Swift). { .fragment }

---

## Resumo da Aula ✅

- Desktop é a fronteira final. { .fragment }
- Performance imbatível. { .fragment }
- Experiência completa com periféricos. { .fragment }

---

## Próxima Aula: Carreira e Projeto Final 🏆

- Como se destacar no mercado? { .fragment }
- Orientação para o TCC do curso. { .fragment }

---

## Dúvidas? 🤔

> "O Flutter transformou o desktop em uma tela familiar para o desenvolvedor mobile."
