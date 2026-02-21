# Aula 15 - Aplicações Desktop 💻
## Flutter Nativo no PC

---

## Agenda de Hoje 📅

1. Status do Desktop no Flutter <!-- .element: class="fragment" -->
2. Requisitos por SO <!-- .element: class="fragment" -->
3. Interações Desktop (Mouse/Teclado) <!-- .element: class="fragment" -->
4. Acesso ao Sistema de Arquivos <!-- .element: class="fragment" -->
5. Compilação e Distribuição <!-- .element: class="fragment" -->

---

## 1. Por que Desktop? 🖥️

- Performance nativa real (64 bits). <!-- .element: class="fragment" -->
- Uso de todo o hardware do PC (GPU/Multi-core). <!-- .element: class="fragment" -->
- Ferramentas internas e sistemas de gestão. <!-- .element: class="fragment" -->

---

## 2. Requisitos Windows 🪟

- Visual Studio instalado. <!-- .element: class="fragment" -->
- Workload de "C++ Desktop Development". <!-- .element: class="fragment" -->

---

## 3. Requisitos macOS 🍎

- Xcode instalado e atualizado. <!-- .element: class="fragment" -->

---

## 4. Requisitos Linux 🐧

- Bibliotecas GTK e Clang configuradas. <!-- .element: class="fragment" -->

---

## 5. Menus e Atalhos de Teclado ⌨️

- Ctrl+S, Ctrl+Z. <!-- .element: class="fragment" -->
- Barra de menus superior (File, Edit). <!-- .element: class="fragment" -->
- Pacote `menubar` ou `shortcut_manager`. <!-- .element: class="fragment" -->

---

## 6. Multi-Window (Múltiplas Janelas) 🪟🪟

- Recentemente adicionado ao Flutter de forma experimental/via pacotes. <!-- .element: class="fragment" -->

---

## 7. Seleção de Arquivos 📂

- Abrir e salvar janelas nativas do sistema. <!-- .element: class="fragment" -->
- Pacote `file_picker`. <!-- .element: class="fragment" -->

---

## 8. Persistência Desktop 💾

- SQLite também funciona aqui! <!-- .element: class="fragment" -->
- Arquivos JSON/Texto locais. <!-- .element: class="fragment" -->

---

## 9. Rodando o Projeto 🚀

```termynal
$ flutter run -d windows
```

---

## 10. O Resultado: Executável Nativo 📦

- Nada de WebView. <!-- .element: class="fragment" -->
- Nada de interpretador lento. <!-- .element: class="fragment" -->
- Apenas código de máquina rodando direto no processador. <!-- .element: class="fragment" -->

---

## 11. Bandeja do Sistema (System Tray) 📥

- Gerenciar o ícone do app perto do relógio. <!-- .element: class="fragment" -->

---

## 12. Tamanho da Janela Inicial 📏

- Definir o tamanho padrão no código nativo (C++ ou Swift). <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Desktop é a fronteira final. <!-- .element: class="fragment" -->
- Performance imbatível. <!-- .element: class="fragment" -->
- Experiência completa com periféricos. <!-- .element: class="fragment" -->

---

## Próxima Aula: Carreira e Projeto Final 🏆

- Como se destacar no mercado? <!-- .element: class="fragment" -->
- Orientação para o TCC do curso. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "O Flutter transformou o desktop em uma tela familiar para o desenvolvedor mobile."
