# Aula 14 - Publicando para Web 🌐
## Flutter nos Navegadores

---

## Agenda de Hoje 📅

1. Habilitando o Suporte Web { .fragment }
2. Renderizadores (HTML vs Canvas) { .fragment }
3. Responsividade no Browser { .fragment }
4. Build e Deploy { .fragment }
5. O que é um PWA? { .fragment }

---

## 1. Flutter Web é Mágica? ✨

- Não! É o seu código Dart sendo transformado em JavaScript e Canvas. { .fragment }

---

## 2. Habilitando a Plataforma 🛠️

```termynal
$ flutter config --enable-web
```
- Surge uma pasta `web/` no seu projeto. { .fragment }

---

## 3. Renderizador HTML 🌐

- Mais leve para carregar. { .fragment }
- Usa elementos padrão do navegador. { .fragment }
- Ideal para sites de texto e imagens simples. { .fragment }

---

## 4. Renderizador CanvasKit 🎨

- Usa WebAssembly e Skia. { .fragment }
- Visual idêntico ao mobile. { .fragment }
- Download inicial mais pesado (~2MB extra). { .fragment }

---

## 5. O Desafio da Tela Grande 💻

- No celular, tudo é vertical. { .fragment }
- Na web, o usuário pode esticar a janela. { .fragment }

---

## 6. LayoutBuilder & MediaQuery 📐

- Ferramentas para perguntar: "Qual a largura da tela agora?". { .fragment }
- Se > 600px, mostre 3 colunas. Se < 600px, mostre uma. { .fragment }

---

## 7. Mouse vs Toque 🖱️

- Adicione `MouseRegion` para efeitos de hover. { .fragment }
- Cursor de "mãozinha" em botões. { .fragment }

---

## 8. Gerando a pasta de Build 📦

```termynal
$ flutter build web --release
```
- O resultado é um index.html e um monte de JS. { .fragment }

---

## 9. Onde hospedar de graça? ☁️

- GitHub Pages. { .fragment }
- Vercel ou Netlify. { .fragment }
- Firebase Hosting. { .fragment }

---

## 10. Flutter como PWA 📲

- Progressive Web App. { .fragment }
- O usuário pode "instalar" o site como se fosse um app no celular. { .fragment }

---

## 11. Navegação via URL 🔗

- Sincronizar o caminho da URL com a página do Fluter. { .fragment }
- `go_router` é o pacote mais indicado para isso. { .fragment }

---

## 12. Cross-Origin (CORS) 🛡️

- Atenção: O navegador bloqueia chamadas de API se o servidor não autorizar o seu domínio. { .fragment }

---

## Resumo da Aula ✅

- Flutter Web amplia seu alcance. { .fragment }
- Responsividade é a alma da web. { .fragment }
- PWA é o melhor dos dois mundos. { .fragment }

---

## Próxima Aula: Aplicações Desktop 💻

- Windows, macOS e Linux nativos. { .fragment }

---

## Dúvidas? 🤔

> "A web não é um lugar, é um estado de espírito multiplataforma."
