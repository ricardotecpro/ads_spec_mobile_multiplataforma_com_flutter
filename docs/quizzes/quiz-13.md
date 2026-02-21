# Quiz 13 - Publicando para Android 🤖

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual arquivo contém as configurações de versão (versionCode e versionName) do app Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O script de build do Gradle (`build.gradle`) é onde definimos os metadados de versão para a Play Store.">main.dart</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O script de build do Gradle (`build.gradle`) é onde definimos os metadados de versão para a Play Store.">pubspec.yaml</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O script de build do Gradle (`build.gradle`) é onde definimos os metadados de versão para a Play Store.">android/app/build.gradle</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O script de build do Gradle (`build.gradle`) é onde definimos os metadados de versão para a Play Store.">AndroidManifest.xml</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para que serve o `minSdkVersion`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se você colocar `minSdkVersion 21`, o app não rodará em versões como Android 4.4.">Define o tamanho máximo do app.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Se você colocar `minSdkVersion 21`, o app não rodará em versões como Android 4.4.">Define a versão mínima do Android necessária para rodar o aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se você colocar `minSdkVersion 21`, o app não rodará em versões como Android 4.4.">Define a cor do ícone.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se você colocar `minSdkVersion 21`, o app não rodará em versões como Android 4.4.">Define a velocidade do processador.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual o formato de arquivo recomendado para subir apps na Google Play Store hoje?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O App Bundle permite que o Google gere APKs otimizados para cada tipo de celular, reduzindo o tamanho do download.">APK</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O App Bundle permite que o Google gere APKs otimizados para cada tipo de celular, reduzindo o tamanho do download.">AAB (Android App Bundle)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O App Bundle permite que o Google gere APKs otimizados para cada tipo de celular, reduzindo o tamanho do download.">EXE</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O App Bundle permite que o Google gere APKs otimizados para cada tipo de celular, reduzindo o tamanho do download.">ZIP</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual comando usamos no terminal para gerar a versão de "venda" (assinada) do app?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `build` compila o app em modo `release`, otimizando o código e removendo debuggers.">flutter run</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `build` compila o app em modo `release`, otimizando o código e removendo debuggers.">flutter create</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O comando `build` compila o app em modo `release`, otimizando o código e removendo debuggers.">flutter build appbundle (ou apk)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comando `build` compila o app em modo `release`, otimizando o código e removendo debuggers.">flutter deploy</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que é uma "Keystore" no contexto Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem a chave de assinatura, o Google Play não aceita o seu aplicativo.">Uma loja de aplicativos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem a chave de assinatura, o Google Play não aceita o seu aplicativo.">Um arquivo de chave digital usado para assinar e garantir a autenticidade do seu app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem a chave de assinatura, o Google Play não aceita o seu aplicativo.">Um teclado virtual.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem a chave de assinatura, o Google Play não aceita o seu aplicativo.">Um comando do Flutter.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Onde configuramos o nome exibido do app e as permissões (como acesso à internet)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Manifesto é o arquivo de "declaração de intenções" do app para o sistema Android.">README.md</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Manifesto é o arquivo de "declaração de intenções" do app para o sistema Android.">AndroidManifest.xml</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Manifesto é o arquivo de "declaração de intenções" do app para o sistema Android.">build.gradle</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Manifesto é o arquivo de "declaração de intenções" do app para o sistema Android.">main.dart</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como o Flutter compila o código Dart para rodar no Android em modo release?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A compilação AOT garante a performance fluida (60fps ou mais) do Flutter.">Converte para JavaScript.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A compilação AOT garante a performance fluida (60fps ou mais) do Flutter.">Roda em um interpretador lento.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A compilação AOT garante a performance fluida (60fps ou mais) do Flutter.">Compilação AOT (Ahead-of-Time) para código de máquina nativo (ARM/x86).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A compilação AOT garante a performance fluida (60fps ou mais) do Flutter.">Não compila, apenas copia os arquivos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o comando para listar os dispositivos (emuladores ou físicos) conectados?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `flutter devices` ajuda a identificar para qual aparelho o código será enviado ao rodar.">flutter list</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `flutter devices` ajuda a identificar para qual aparelho o código será enviado ao rodar.">flutter devices</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `flutter devices` ajuda a identificar para qual aparelho o código será enviado ao rodar.">flutter show</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `flutter devices` ajuda a identificar para qual aparelho o código será enviado ao rodar.">adb help</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Por que é importante testar o app em um dispositivo físico real?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comportamento térmico e de memória de um celular real pode ser muito diferente de um PC potente rodando um emulador.">Porque é mais bonito.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O comportamento térmico e de memória de um celular real pode ser muito diferente de um PC potente rodando um emulador.">Emuladores não refletem perfeitamente o consumo de bateria, limitações de hardware e gestos reais do usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comportamento térmico e de memória de um celular real pode ser muito diferente de um PC potente rodando um emulador.">O emulador paga mensalidade.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O comportamento térmico e de memória de um celular real pode ser muito diferente de um PC potente rodando um emulador.">O emulador não acessa a internet.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que o modo `--split-per-abi` faz ao criar um APK?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para distribuir versões leves fora da Play Store.">Divide o código ao meio.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Útil para distribuir versões leves fora da Play Store.">Gera APKs separados para diferentes arquiteturas de processador, reduzindo o tamanho final de cada arquivo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para distribuir versões leves fora da Play Store.">Apaga o projeto original.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para distribuir versões leves fora da Play Store.">Muda o idioma para inglês.</div>
  <div class="quiz-feedback"></div>
</div>
