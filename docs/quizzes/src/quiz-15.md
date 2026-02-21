# Quiz 15 - Aplicações Desktop 💻

1. Quais sistemas operacionais de desktop o Flutter suporta?
    - [ ] Apenas Windows.
    - [x] Windows, macOS e Linux.
    - [ ] Apenas macOS.
    - [ ] Windows e Web.
    *Explicação: O Flutter expandiu para os três principais sistemas operacionais de desktop.*

2. Qual ferramenta extra é necessária para compilar apps Flutter para Windows?
    - [ ] JDK (Java)
    - [ ] Python
    - [x] Visual Studio (com C++ desktop development)
    - [ ] Xcode
    *Explicação: O Windows exige o compilador C++ da Microsoft para gerar o executável nativo.*

3. Como habilitamos o suporte para Windows se ele estiver desativado?
    - [ ] flutter windows on
    - [x] flutter config --enable-windows-desktop
    - [ ] flutter build windows
    - [ ] Instalar o Windows de novo.
    *Explicação: Através do comando `config` habilitamos as plataformas desejadas no SDK.*

4. No desktop, qual o comportamento esperado de um app quando a janela é redimensionada?
    - [ ] Ele deve fechar.
    - [x] Ele deve ser responsivo e adaptar seu layout ao novo tamanho da janela.
    - [ ] Ele deve ficar esticado.
    - [ ] Nada acontece.
    *Explicação: Janelas de computador são muito mais dinâmicas que telas de celular.*

5. Qual a diferença de navegação principal entre mobile e desktop?
    - [ ] Desktop não tem botões.
    - [x] Desktop frequentemente usa menus laterais (Sidebar) fixos, enquanto mobile usa menus inferiores ou gavetas (Drawer).
    - [ ] Mobile é mais rápido.
    - [ ] Não há diferença.
    *Explicação: O espaço extra no desktop permite layouts de navegação persistentes.*

6. Qual objeto usamos no Flutter para detectar quando o mouse passa por cima de um widget?
    - [ ] ClickDetector
    - [ ] TapRegion
    - [x] MouseRegion (onHover/onEnter/onExit)
    - [ ] EyeTracker
    *Explicação: `MouseRegion` é o widget específico para capturar eventos exclusivos do mouse.*

7. Para que servem os atalhos de teclado (Keyboard Shortcuts) no desktop?
    - [ ] Para economizar bateria.
    - [x] Para aumentar a produtividade do usuário (ex: Ctrl+C, Ctrl+V, Esc).
    - [ ] Para jogar videogame.
    - [ ] Não existem no Flutter.
    *Explicação: Aplicativos desktop profissionais sempre oferecem atalhos para funções comuns.*

8. O que o Flutter gera ao final de um build para Windows?
    - [ ] Um arquivo .apk.
    - [x] Uma pasta contendo um arquivo `.exe` e todas as bibliotecas `.dll` necessárias.
    - [ ] Um site.
    - [ ] Um vídeo do app.
    *Explicação: É gerado um executável nativo de 64 bits.*

9. O Flutter tem acesso ao sistema de arquivos (Pastas, Arquivos) no desktop?
    - [ ] Não, por segurança.
    - [x] Sim, através de pacotes como `path_provider` e pacotes nativos de seleção de arquivos.
    - [ ] Apenas se o usuário for administrador.
    - [ ] Apenas no Linux.
    *Explicação: Diferente dos navegadores, apps desktop podem ler e escrever livremente no disco (com permissão).*

10. Como testamos o app rodando como uma aplicação Windows?
    - [ ] flutter run -d chrome
    - [x] flutter run -d windows
    - [ ] dart bin/main.dart
    - [ ] Carregando no pendrive.
    *Explicação: O comando `run` com o target `windows` inicia o processo nativo de depuração.*
