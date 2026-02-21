# Aula 13 - Publicando para Android 🤖
## Do Código à Play Store

---

## Agenda de Hoje 📅

1. Ciclo de Release <!-- .element: class="fragment" -->
2. Ícone e Nome do App <!-- .element: class="fragment" -->
3. Versão e build.gradle <!-- .element: class="fragment" -->
4. Keystone e Assinatura <!-- .element: class="fragment" -->
5. Gerando o APK/Bundle <!-- .element: class="fragment" -->

---

## 1. Modo Debug vs Mode Release ⚔️

- Debug: Lento, pesado, possui o "banner" no canto. <!-- .element: class="fragment" -->
- Release: Rápido, código ofuscado e otimizado para o usuário. <!-- .element: class="fragment" -->

---

## 2. Vestindo o App: Ícones 🎨

- Pacote `flutter_launcher_icons`. <!-- .element: class="fragment" -->
- Gera ícones para todas as resoluções Android de uma vez. <!-- .element: class="fragment" -->

---

## 3. O Nome na Tela de Início 📛

- Editamos o `label` no arquivo `AndroidManifest.xml`. <!-- .element: class="fragment" -->

---

## 4. Gerenciando Versões 🔢

- `versionName`: O que o usuário vê (ex: 1.0.0). <!-- .element: class="fragment" -->
- `versionCode`: Um número inteiro que sobe a cada build (ex: 1, 2, 3). <!-- .element: class="fragment" -->

---

## 5. Por que assinar o app? 🖋️

- Garante que você é o autor original. <!-- .element: class="fragment" -->
- Impede que terceiros modifiquem seu código e subam uma "atualização" falsa. <!-- .element: class="fragment" -->

---

## 6. Criando a Keystore 🔑

```termynal
$ keytool -genkey -v -keystore meu-app.jks ...
```
- Guarde este arquivo em um lugar seguro (nuvem/backup). Perdê-lo significa nunca mais conseguir atualizar o app. <!-- .element: class="fragment" -->

---

## 7. Configurando build.gradle ⚙️

- Onde "contamos" para o Android onde está a nossa chave secreta. <!-- .element: class="fragment" -->

---

## 8. APK vs App Bundle (AAB) ⚖️

- APK: Um arquivo gigante que serve para todos. <!-- .element: class="fragment" -->
- AAB: Arquivo inteligente que o Google usa para gerar pedaços menores para cada celular. <!-- .element: class="fragment" -->

---

## 9. Comando de Build 🚀

```termynal
$ flutter build appbundle
```
- O arquivo final será gerado em `build/app/outputs/bundle/release/`. <!-- .element: class="fragment" -->

---

## 10. Testando a Performance Real ⚡

- Apps em modo release rodam muito mais rápido que em debug. <!-- .element: class="fragment" -->

---

## 11. O Console da Google Play 🏪

- Onde você sobe o arquivo, define preço, países e capturas de tela. <!-- .element: class="fragment" -->

---

## 12. Permissões de Sistema 🛡️

- Internet, GPS, Câmera. Tudo deve ser declarado antes do build final. <!-- .element: class="fragment" -->

---

## Resumo da Aula ✅

- Build de produção é o destino final. <!-- .element: class="fragment" -->
- Identidade visual é o ícone. <!-- .element: class="fragment" -->
- Assinatura digital é sua garantia de autoria. <!-- .element: class="fragment" -->

---

## Próxima Aula: Publicando para Web 🌐

- Saindo dos celulares e indo para os navegadores. <!-- .element: class="fragment" -->

---

## Dúvidas? 🤔

> "Lançar um aplicativo é o começo, não o fim da jornada."
