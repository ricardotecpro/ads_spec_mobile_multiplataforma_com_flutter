# Quiz 13 - Publicando para Android 🤖

1. Qual arquivo contém as configurações de versão (versionCode e versionName) do app Android?
    - [ ] main.dart
    - [ ] pubspec.yaml
    - [x] android/app/build.gradle
    - [ ] AndroidManifest.xml
    *Explicação: O script de build do Gradle (`build.gradle`) é onde definimos os metadados de versão para a Play Store.*

2. Para que serve o `minSdkVersion`?
    - [ ] Define o tamanho máximo do app.
    - [x] Define a versão mínima do Android necessária para rodar o aplicativo.
    - [ ] Define a cor do ícone.
    - [ ] Define a velocidade do processador.
    *Explicação: Se você colocar `minSdkVersion 21`, o app não rodará em versões como Android 4.4.*

3. Qual o formato de arquivo recomendado para subir apps na Google Play Store hoje?
    - [ ] APK
    - [x] AAB (Android App Bundle)
    - [ ] EXE
    - [ ] ZIP
    *Explicação: O App Bundle permite que o Google gere APKs otimizados para cada tipo de celular, reduzindo o tamanho do download.*

4. Qual comando usamos no terminal para gerar a versão de "venda" (assinada) do app?
    - [ ] flutter run
    - [ ] flutter create
    - [x] flutter build appbundle (ou apk)
    - [ ] flutter deploy
    *Explicação: O comando `build` compila o app em modo `release`, otimizando o código e removendo debuggers.*

5. O que é uma "Keystore" no contexto Android?
    - [ ] Uma loja de aplicativos.
    - [x] Um arquivo de chave digital usado para assinar e garantir a autenticidade do seu app.
    - [ ] Um teclado virtual.
    - [ ] Um comando do Flutter.
    *Explicação: Sem a chave de assinatura, o Google Play não aceita o seu aplicativo.*

6. Onde configuramos o nome exibido do app e as permissões (como acesso à internet)?
    - [ ] README.md
    - [x] AndroidManifest.xml
    - [ ] build.gradle
    - [ ] main.dart
    *Explicação: O Manifesto é o arquivo de "declaração de intenções" do app para o sistema Android.*

7. Como o Flutter compila o código Dart para rodar no Android em modo release?
    - [ ] Converte para JavaScript.
    - [ ] Roda em um interpretador lento.
    - [x] Compilação AOT (Ahead-of-Time) para código de máquina nativo (ARM/x86).
    - [ ] Não compila, apenas copia os arquivos.
    *Explicação: A compilação AOT garante a performance fluida (60fps ou mais) do Flutter.*

8. Qual o comando para listar os dispositivos (emuladores ou físicos) conectados?
    - [ ] flutter list
    - [x] flutter devices
    - [ ] flutter show
    - [ ] adb help
    *Explicação: `flutter devices` ajuda a identificar para qual aparelho o código será enviado ao rodar.*

9. Por que é importante testar o app em um dispositivo físico real?
    - [ ] Porque é mais bonito.
    - [x] Emuladores não refletem perfeitamente o consumo de bateria, limitações de hardware e gestos reais do usuário.
    - [ ] O emulador paga mensalidade.
    - [ ] O emulador não acessa a internet.
    *Explicação: O comportamento térmico e de memória de um celular real pode ser muito diferente de um PC potente rodando um emulador.*

10. O que o modo `--split-per-abi` faz ao criar um APK?
    - [ ] Divide o código ao meio.
    - [x] Gera APKs separados para diferentes arquiteturas de processador, reduzindo o tamanho final de cada arquivo.
    - [ ] Apaga o projeto original.
    - [ ] Muda o idioma para inglês.
    *Explicação: Útil para distribuir versões leves fora da Play Store.*
