# Quiz 14 - Publicando para Web 🌐

1. O Flutter Web utiliza qual linguagem como resultado final do build?
    - [ ] C++
    - [ ] Java
    - [x] JavaScript (além de HTML/CSS)
    - [ ] Python
    *Explicação: Para rodar no navegador, o código Dart é transpilado para JavaScript.*

2. Qual widget é fundamental para criar layouts que se adaptam a diferentes tamanhos de janela de navegador?
    - [ ] Flexible
    - [x] LayoutBuilder
    - [ ] PageView
    - [ ] Scaffold
    *Explicação: O `LayoutBuilder` permite que você tome decisões baseadas na largura e altura da "janela" atual.*

3. Qual a principal diferença entre os renderizadores HTML e CanvasKit?
    - [ ] HTML é mais pesado.
    - [x] CanvasKit oferece maior fidelidade visual e performance, mas gera um download inicial maior (WebAssembly).
    - [ ] HTML não suporta botões.
    - [ ] CanvasKit só funciona no Firefox.
    *Explicação: CanvasKit usa WebAssembly para desenhar a interface exatamente como no mobile.*

4. Qual pasta é gerada após o comando `flutter build web`?
    - [ ] bin/web
    - [ ] dist/
    - [x] build/web/
    - [ ] out/web
    *Explicação: Esta pasta contém o `index.html` e todos os recursos prontos para serem hospedados em um servidor.*

5. O que significa "Hospedagem Estática" (Static Hosting)?
    - [ ] Um servidor que não se move.
    - [x] Servidores que entregam arquivos HTML/JS/CSS puros sem processamento no lado do servidor (ex: GitHub Pages).
    - [ ] Um banco de dados SQL online.
    - [ ] Onde se guardam cabos de rede.
    *Explicação: Como o Flutter Web é apenas um conjunto de arquivos, ele pode ser hospedado de forma barata ou gratuita.*

6. Como configuramos a URL base do app web (importante para o carregamento de imagens)?
    - [ ] No main.dart.
    - [x] No parâmetro `--base-href` do comando de build ou via tag `<base>` no index.html.
    - [ ] No WhatsApp do Google.
    - [ ] Não é necessário configurar.
    *Explicação: Sem a base-href correta, o navegador pode se perder ao tentar achar os scripts do app.*

7. É possível transformar um app Flutter Web em um PWA (Progressive Web App)?
    - [ ] Não, Flutter não suporta PWAs.
    - [x] Sim, o Flutter gera automaticamente o `manifest.json` e o `service worker` para isso.
    - [ ] Apenas se usar JavaScript puro.
    - [ ] Sim, mas só no Android.
    *Explicação: PWAs permitem que o app web seja instalado no celular e funcione parcialmente offline.*

8. Qual o comando para rodar o app no navegador Chrome durante o desenvolvimento?
    - [ ] flutter start
    - [x] flutter run -d chrome
    - [ ] dart web
    - [ ] open index.html
    *Explicação: O Flutter SDK se conecta ao Chrome para permitir o debug e o hot reload na web.*

9. Por que o SEO é um desafio no Flutter Web?
    - [ ] O Google não gosta de Flutter.
    - [x] Pois o conteúdo é desenhado dinamicamente via JS/Canvas, dificultando a leitura simples pelos robôs de busca.
    - [ ] Porque os códigos são criptografados.
    - [ ] Porque não usa imagens.
    *Explicação: Embora esteja melhorando, o Flutter Web ainda é mais focado em web apps do que em sites de conteúdo.*

10. O suporte para Web no Flutter é habilitado por padrão em novas instalações?
    - [ ] Não, precisa de um plugin pago.
    - [x] Sim, em versões estáveis recentes do Flutter (Canal Stable).
    - [ ] Apenas no Linux.
    - [ ] Só se você tiver o Chrome instalado.
    *Explicação: Atualmente o suporte web é estável e vem ativado de fábrica.*
