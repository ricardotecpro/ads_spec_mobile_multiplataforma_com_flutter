# Quiz 14 - Publicando para Web 🌐

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O Flutter Web utiliza qual linguagem como resultado final do build?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para rodar no navegador, o código Dart é transpilado para JavaScript.">C++</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para rodar no navegador, o código Dart é transpilado para JavaScript.">Java</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Para rodar no navegador, o código Dart é transpilado para JavaScript.">JavaScript (além de HTML/CSS)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para rodar no navegador, o código Dart é transpilado para JavaScript.">Python</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual widget é fundamental para criar layouts que se adaptam a diferentes tamanhos de janela de navegador?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `LayoutBuilder` permite que você tome decisões baseadas na largura e altura da "janela" atual.">Flexible</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O `LayoutBuilder` permite que você tome decisões baseadas na largura e altura da "janela" atual.">LayoutBuilder</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `LayoutBuilder` permite que você tome decisões baseadas na largura e altura da "janela" atual.">PageView</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O `LayoutBuilder` permite que você tome decisões baseadas na largura e altura da "janela" atual.">Scaffold</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal diferença entre os renderizadores HTML e CanvasKit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. CanvasKit usa WebAssembly para desenhar a interface exatamente como no mobile.">HTML é mais pesado.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! CanvasKit usa WebAssembly para desenhar a interface exatamente como no mobile.">CanvasKit oferece maior fidelidade visual e performance, mas gera um download inicial maior (WebAssembly).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. CanvasKit usa WebAssembly para desenhar a interface exatamente como no mobile.">HTML não suporta botões.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. CanvasKit usa WebAssembly para desenhar a interface exatamente como no mobile.">CanvasKit só funciona no Firefox.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual pasta é gerada após o comando `flutter build web`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Esta pasta contém o `index.html` e todos os recursos prontos para serem hospedados em um servidor.">bin/web</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Esta pasta contém o `index.html` e todos os recursos prontos para serem hospedados em um servidor.">dist/</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Esta pasta contém o `index.html` e todos os recursos prontos para serem hospedados em um servidor.">build/web/</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Esta pasta contém o `index.html` e todos os recursos prontos para serem hospedados em um servidor.">out/web</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que significa "Hospedagem Estática" (Static Hosting)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como o Flutter Web é apenas um conjunto de arquivos, ele pode ser hospedado de forma barata ou gratuita.">Um servidor que não se move.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Como o Flutter Web é apenas um conjunto de arquivos, ele pode ser hospedado de forma barata ou gratuita.">Servidores que entregam arquivos HTML/JS/CSS puros sem processamento no lado do servidor (ex: GitHub Pages).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como o Flutter Web é apenas um conjunto de arquivos, ele pode ser hospedado de forma barata ou gratuita.">Um banco de dados SQL online.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Como o Flutter Web é apenas um conjunto de arquivos, ele pode ser hospedado de forma barata ou gratuita.">Onde se guardam cabos de rede.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Como configuramos a URL base do app web (importante para o carregamento de imagens)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem a base-href correta, o navegador pode se perder ao tentar achar os scripts do app.">No main.dart.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem a base-href correta, o navegador pode se perder ao tentar achar os scripts do app.">No parâmetro `--base-href` do comando de build ou via tag `<base>` no index.html.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem a base-href correta, o navegador pode se perder ao tentar achar os scripts do app.">No WhatsApp do Google.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem a base-href correta, o navegador pode se perder ao tentar achar os scripts do app.">Não é necessário configurar.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. É possível transformar um app Flutter Web em um PWA (Progressive Web App)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. PWAs permitem que o app web seja instalado no celular e funcione parcialmente offline.">Não, Flutter não suporta PWAs.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! PWAs permitem que o app web seja instalado no celular e funcione parcialmente offline.">Sim, o Flutter gera automaticamente o `manifest.json` e o `service worker` para isso.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. PWAs permitem que o app web seja instalado no celular e funcione parcialmente offline.">Apenas se usar JavaScript puro.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. PWAs permitem que o app web seja instalado no celular e funcione parcialmente offline.">Sim, mas só no Android.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o comando para rodar o app no navegador Chrome durante o desenvolvimento?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter SDK se conecta ao Chrome para permitir o debug e o hot reload na web.">flutter start</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Flutter SDK se conecta ao Chrome para permitir o debug e o hot reload na web.">flutter run -d chrome</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter SDK se conecta ao Chrome para permitir o debug e o hot reload na web.">dart web</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter SDK se conecta ao Chrome para permitir o debug e o hot reload na web.">open index.html</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Por que o SEO é um desafio no Flutter Web?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora esteja melhorando, o Flutter Web ainda é mais focado em web apps do que em sites de conteúdo.">O Google não gosta de Flutter.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Embora esteja melhorando, o Flutter Web ainda é mais focado em web apps do que em sites de conteúdo.">Pois o conteúdo é desenhado dinamicamente via JS/Canvas, dificultando a leitura simples pelos robôs de busca.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora esteja melhorando, o Flutter Web ainda é mais focado em web apps do que em sites de conteúdo.">Porque os códigos são criptografados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora esteja melhorando, o Flutter Web ainda é mais focado em web apps do que em sites de conteúdo.">Porque não usa imagens.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O suporte para Web no Flutter é habilitado por padrão em novas instalações?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Atualmente o suporte web é estável e vem ativado de fábrica.">Não, precisa de um plugin pago.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Atualmente o suporte web é estável e vem ativado de fábrica.">Sim, em versões estáveis recentes do Flutter (Canal Stable).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Atualmente o suporte web é estável e vem ativado de fábrica.">Apenas no Linux.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Atualmente o suporte web é estável e vem ativado de fábrica.">Só se você tiver o Chrome instalado.</div>
  <div class="quiz-feedback"></div>
</div>
