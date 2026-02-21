# Aula 13 - Publicando para Android 🤖
## Do Código à Play Store

---

## Agenda de Hoje 📅

1. Ciclo de Release { .fragment }
2. Ícone e Nome do App { .fragment }
3. Versão e build.gradle { .fragment }
4. Keystone e Assinatura { .fragment }
5. Gerando o APK/Bundle { .fragment }

---

## 1. Modo Debug vs Mode Release ⚔️

- Debug: Lento, pesado, possui o "banner" no canto. { .fragment }
- Release: Rápido, código ofuscado e otimizado para o usuário. { .fragment }

---

## 2. Vestindo o App: Ícones 🎨

- Pacote `flutter_launcher_icons`. { .fragment }
- Gera ícones para todas as resoluções Android de uma vez. { .fragment }

---

## 3. O Nome na Tela de Início 📛

- Editamos o `label` no arquivo `AndroidManifest.xml`. { .fragment }

---

## 4. Gerenciando Versões 🔢

- `versionName`: O que o usuário vê (ex: 1.0.0). { .fragment }
- `versionCode`: Um número inteiro que sobe a cada build (ex: 1, 2, 3). { .fragment }

---

## 5. Por que assinar o app? 🖋️

- Garante que você é o autor original. { .fragment }
- Impede que terceiros modifiquem seu código e subam uma "atualização" falsa. { .fragment }

---

## 6. Criando a Keystore 🔑

```termynal
$ keytool -genkey -v -keystore meu-app.jks ...
```
- Guarde este arquivo em um lugar seguro (nuvem/backup). Perdê-lo significa nunca mais conseguir atualizar o app. { .fragment }

---

## 7. Configurando build.gradle ⚙️

- Onde "contamos" para o Android onde está a nossa chave secreta. { .fragment }

---

## 8. APK vs App Bundle (AAB) ⚖️

- APK: Um arquivo gigante que serve para todos. { .fragment }
- AAB: Arquivo inteligente que o Google usa para gerar pedaços menores para cada celular. { .fragment }

---

## 9. Comando de Build 🚀

```termynal
$ flutter build appbundle
```
- O arquivo final será gerado em `build/app/outputs/bundle/release/`. { .fragment }

---

## 10. Testando a Performance Real ⚡

- Apps em modo release rodam muito mais rápido que em debug. { .fragment }

---

## 11. O Console da Google Play 🏪

- Onde você sobe o arquivo, define preço, países e capturas de tela. { .fragment }

---

## 12. Permissões de Sistema 🛡️

- Internet, GPS, Câmera. Tudo deve ser declarado antes do build final. { .fragment }

---

## Resumo da Aula ✅

- Build de produção é o destino final. { .fragment }
- Identidade visual é o ícone. { .fragment }
- Assinatura digital é sua garantia de autoria. { .fragment }

---

## Próxima Aula: Publicando para Web 🌐

- Saindo dos celulares e indo para os navegadores. { .fragment }

---

## Dúvidas? 🤔

> "Lançar um aplicativo é o começo, não o fim da jornada."
