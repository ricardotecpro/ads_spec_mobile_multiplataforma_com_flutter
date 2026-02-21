# Quiz 15 - Aplicações Desktop 💻

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Quais sistemas operacionais de desktop o Flutter suporta?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter expandiu para os três principais sistemas operacionais de desktop.">Apenas Windows.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Flutter expandiu para os três principais sistemas operacionais de desktop.">Windows, macOS e Linux.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter expandiu para os três principais sistemas operacionais de desktop.">Apenas macOS.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Flutter expandiu para os três principais sistemas operacionais de desktop.">Windows e Web.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual ferramenta extra é necessária para compilar apps Flutter para Windows?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Windows exige o compilador C++ da Microsoft para gerar o executável nativo.">JDK (Java)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Windows exige o compilador C++ da Microsoft para gerar o executável nativo.">Python</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Windows exige o compilador C++ da Microsoft para gerar o executável nativo.">Visual Studio (com C++ desktop development)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Windows exige o compilador C++ da Microsoft para gerar o executável nativo.">Xcode</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Como habilitamos o suporte para Windows se ele estiver desativado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Através do comando `config` habilitamos as plataformas desejadas no SDK.">flutter windows on</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Através do comando `config` habilitamos as plataformas desejadas no SDK.">flutter config --enable-windows-desktop</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Através do comando `config` habilitamos as plataformas desejadas no SDK.">flutter build windows</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Através do comando `config` habilitamos as plataformas desejadas no SDK.">Instalar o Windows de novo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. No desktop, qual o comportamento esperado de um app quando a janela é redimensionada?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Janelas de computador são muito mais dinâmicas que telas de celular.">Ele deve fechar.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Janelas de computador são muito mais dinâmicas que telas de celular.">Ele deve ser responsivo e adaptar seu layout ao novo tamanho da janela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Janelas de computador são muito mais dinâmicas que telas de celular.">Ele deve ficar esticado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Janelas de computador são muito mais dinâmicas que telas de celular.">Nada acontece.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a diferença de navegação principal entre mobile e desktop?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O espaço extra no desktop permite layouts de navegação persistentes.">Desktop não tem botões.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O espaço extra no desktop permite layouts de navegação persistentes.">Desktop frequentemente usa menus laterais (Sidebar) fixos, enquanto mobile usa menus inferiores ou gavetas (Drawer).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O espaço extra no desktop permite layouts de navegação persistentes.">Mobile é mais rápido.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O espaço extra no desktop permite layouts de navegação persistentes.">Não há diferença.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual objeto usamos no Flutter para detectar quando o mouse passa por cima de um widget?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `MouseRegion` é o widget específico para capturar eventos exclusivos do mouse.">ClickDetector</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `MouseRegion` é o widget específico para capturar eventos exclusivos do mouse.">TapRegion</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `MouseRegion` é o widget específico para capturar eventos exclusivos do mouse.">MouseRegion (onHover/onEnter/onExit)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `MouseRegion` é o widget específico para capturar eventos exclusivos do mouse.">EyeTracker</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Para que servem os atalhos de teclado (Keyboard Shortcuts) no desktop?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Aplicativos desktop profissionais sempre oferecem atalhos para funções comuns.">Para economizar bateria.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Aplicativos desktop profissionais sempre oferecem atalhos para funções comuns.">Para aumentar a produtividade do usuário (ex: Ctrl+C, Ctrl+V, Esc).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Aplicativos desktop profissionais sempre oferecem atalhos para funções comuns.">Para jogar videogame.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Aplicativos desktop profissionais sempre oferecem atalhos para funções comuns.">Não existem no Flutter.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que o Flutter gera ao final de um build para Windows?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É gerado um executável nativo de 64 bits.">Um arquivo .apk.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É gerado um executável nativo de 64 bits.">Uma pasta contendo um arquivo `.exe` e todas as bibliotecas `.dll` necessárias.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É gerado um executável nativo de 64 bits.">Um site.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É gerado um executável nativo de 64 bits.">Um vídeo do app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O Flutter tem acesso ao sistema de arquivos (Pastas, Arquivos) no desktop?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente dos navegadores, apps desktop podem ler e escrever livremente no disco (com permissão).">Não, por segurança.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Diferente dos navegadores, apps desktop podem ler e escrever livremente no disco (com permissão).">Sim, através de pacotes como `path_provider` e pacotes nativos de seleção de arquivos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente dos navegadores, apps desktop podem ler e escrever livremente no disco (com permissão).">Apenas se o usuário for administrador.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente dos navegadores, apps desktop podem ler e escrever livremente no disco (com permissão).">Apenas no Linux.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como testamos o app rodando como uma aplicação Windows?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `run` com o target `windows` inicia o processo nativo de depuração.">flutter run -d chrome</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O comando `run` com o target `windows` inicia o processo nativo de depuração.">flutter run -d windows</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `run` com o target `windows` inicia o processo nativo de depuração.">dart bin/main.dart</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `run` com o target `windows` inicia o processo nativo de depuração.">Carregando no pendrive.</div>
  <div class="quiz-feedback"></div>
</div>
