# Aula 14 - Publicando para Web 🌐
## Flutter nos Navegadores

---

## Agenda de Hoje 📅

1. Habilitando o Suporte Web <!-- .element: class="fragment" -->
2. Renderizadores (HTML vs Canvas) <!-- .element: class="fragment" -->
3. Responsividade no Browser <!-- .element: class="fragment" -->
4. Build e Deploy <!-- .element: class="fragment" -->
5. O que é um PWA? <!-- .element: class="fragment" -->

---

## 1. Flutter Web é Mágica? ✨

- Não! É o seu código Dart sendo transformado em JavaScript e Canvas. <!-- .element: class="fragment" -->

---

## 2. Habilitando a Plataforma 🛠️

```termynal
$ flutter config --enable-web
```
- Surge uma pasta `web/` no seu projeto. <!-- .element: class="fragment" -->

---

## 3. Renderizador HTML 🌐

- Mais leve para carregar. <!-- .element: class="fragment" -->
- Usa elementos padrão do navegador. <!-- .element: class="fragment" -->
- Ideal para sites de texto e imagens simples. <!-- .element: class="fragment" -->

---

## 4. Renderizador CanvasKit 🎨

- Usa WebAssembly e Skia. <!-- .element: class="fragment" -->
- Visual idêntico ao mobile. <!-- .element: class="fragment" -->
- Download inicial mais pesado (~2MB extra). <!-- .element: class="fragment" -->

---

## 5. O Desafio da Tela Grande 💻

- No celular, tudo é vertical. <!-- .element: class="fragment" -->
- Na web, o usuário pode esticar a janela. <!-- .element: class="fragment" -->

---

## 6. LayoutBuilder & MediaQuery 📐

- Ferramentas para perguntar: "Qual a largura da tela agora?". <!-- .element: class="fragment" -->
- Se > 600px, mostre 3 colunas. Se < 600px, mostre uma. <!-- .element: class="fragment" -->

---

## 7. Mouse vs Toque 🖱️

- Adicione `MouseRegion` para efeitos de hover. <!-- .element: class="fragment" -->
- Cursor de "mãozinha" em botões. <!-- .element: class="fragment" -->

---

## 8. Gerando a pasta de Build 📦

```termynal
$ flutter build web --release
```
- O resultado é um index.html e um monte de JS. <!-- .element: class="fragment" -->

---

## 9. Onde hospedar de graça? ☁️

- GitHub Pages. <!-- .element: class="fragment" -->
- Vercel ou Netlify. <!-- .element: class="fragment" -->
- Firebase Hosting. <!-- .element: class="fragment" -->

---

## 10. Flutter como PWA 📲

- Progressive Web App. <!-- .element: class="fragment" -->
- O usuário pode "instalar" o site como se fosse um app no celular. <!-- .element: class="fragment" -->

---

## 11. Navegação via URL 🔗

- Sincronizar o caminho da URL com a página do Fluter. <!-- .element: class="fragment" -->
- `go_router` é o pacote mais indicado para isso. <!-- .element: class="fragment" -->

---

## 12. Cross-Origin (CORS) 🛡️

- Atenção: O navegador bloqueia chamadas de API se o servidor não autorizar o seu domínio. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Flutter Web amplia seu alcance. <!-- .element: class="fragment" -->
- Responsividade é a alma da web. <!-- .element: class="fragment" -->
- PWA é o melhor dos dois mundos. <!-- .element: class="fragment" -->

---

## Próxima Aula: Aplicações Desktop 💻

- Windows, macOS e Linux nativos. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "A web não é um lugar, é um estado de espírito multiplataforma."
