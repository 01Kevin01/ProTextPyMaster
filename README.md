# ProTextPyMaster
![foto_no_exif](https://github.com/01Kevin01/ProTextPyMaster/assets/131346373/e73e19f7-f983-4724-8cd8-62b74f30b29a)

-------------------------------------------------------------------------------------------------------------------------------------------------
Bu kod, kullanıcıya metin şifreleme ve şifrelenmiş metinleri çözme yeteneği sağlayan bir konsol uygulamasını uygular. Aşağıda kodun ana işlevleri açıklanmıştır:

1. **Anahtar Oluşturma ve Yükleme (generate_keys ve load_keys fonksiyonları):**
   - `generate_keys`: RSA şifreleme için bir çift anahtar oluşturur (2048 bit uzunluğunda). Oluşturulan özel anahtar (`private_key`) ve genel anahtar (`public_key`) dosyalara kaydedilir.
   - `load_keys`: Eğer daha önce anahtarlar zaten oluşturulmuşsa, bu anahtarları diskten yükler. Aksi takdirde yeni anahtarlar oluşturur ve kaydeder.

2. **Metni RSA ile Şifreleme ve Çözme (rsa_encrypt_text ve rsa_decrypt_text fonksiyonları):**
   - `rsa_encrypt_text`: Verilen genel anahtarla metni RSA ile şifreler ve şifrelenmiş metni döndürür.
   - `rsa_decrypt_text`: Verilen özel anahtarla şifrelenmiş metni çözer ve orijinal metni döndürür.

3. **Metni AES ile Şifreleme ve Çözme (aes_encrypt_text ve aes_decrypt_text fonksiyonları):**
   - `aes_encrypt_text`: Verilen AES anahtarı ile metni AES kullanarak şifreler ve şifrelenmiş metni döndürür. AES, belirtilen anahtarı kullanarak veriyi şifreler ve bir rastgele sayı üreterek kullanır (nonce).
   - `aes_decrypt_text`: Verilen AES anahtarı ile şifrelenmiş metni çözer ve orijinal metni döndürür.

4. **Anahtar ve Şifreleme İşlemleri ile İlgili Menü (show_menu fonksiyonu):**
   - Bu fonksiyon, kullanıcıya şifreleme ve şifre çözme seçeneklerini sunar.
   - Kullanıcı, metin şifreleme ve çözme işlemlerini gerçekleştirebilir veya programdan çıkabilir.

5. **Anahtar ve Şifre Kontrolü:**
   - Eğer "master_password.txt" adında bir dosya bulunuyorsa, bu dosyadaki RSA ile şifrelenmiş kullanıcı adı ve anahtarını okur.
   - Kullanıcıdan kullanıcı adı ve anahtar girişi alır.
   - Giriş doğrulandığında ana menüyü gösterir.

Bu kod, kullanıcıların metinlerini şifrelemelerine ve şifrelenmiş metinleri çözmelerine olanak tanır.
Ayrıca bir "ana şifre" ile korunur, bu nedenle kullanıcılar giriş yapmadan önce bu ana şifreyi girmelidirler.
Ayrıca kullanıcı adı ve anahtarlar RSA ile şifrelenir ve güvenli bir şekilde saklanır. Bu kodun amacı gizli verileri korumaktır. 

GitHub README dosyanızda kullanım talimatlarını aşağıdaki gibi yazabilirsiniz:

# Kripto Metin İşleme Uygulaması

Bu uygulama, metinleri şifrelemek ve şifrelenmiş metinleri çözmek için kullanabileceğiniz bir konsol uygulamasıdır. Aşağıda, uygulamanın nasıl kullanılacağına dair adımları bulabilirsiniz.

## Kurulum

1. Bu uygulamayı bilgisayarınıza klonlayın veya ZIP dosyasını indirin.
2. Uygulamanın ana dizinine gidin.

## Anahtar Oluşturma

Uygulamayı kullanmadan önce RSA anahtar çiftini ve bir "ana şifre"yi oluşturmanız gerekmektedir.

1. Anahtarları oluşturmak için uygulamayı başlatın:
   ```
   python ProTextPyMaster.py
   ```
2. İlk başta, size yeni bir anahtar çifti oluşturup oluşturmadığınızı soracaktır. "E" veya "H" seçeneğine basarak anahtarları oluşturun.

## Ana Şifre Oluşturma veya Giriş

1. İlk çalıştırmada, ana şifre belirlemeniz istenecektir. Bu ana şifre, şifrelenmiş verilere erişim sağlar. Giriş yapmak için bu şifreyi kullanacaksınız.
2. Kullanıcı adınızı ve ana şifrenizi girdikten sonra, ana menüye erişebilirsiniz.

## Metin Şifreleme ve Çözme

Ana menüde aşağıdaki seçenekleri bulacaksınız:

1. **Metin Şifrele ve Kaydet**
   - Bu seçenekle metinleri AES ile şifreleyebilir ve şifrelenmiş metni bir dosyada kaydedebilirsiniz.

2. **Şifrelenmiş Metni Çöz**
   - Bu seçenekle şifrelenmiş metinleri çözebilirsiniz.

3. **Çıkış**
   - Uygulamadan çıkış yapar.

Her seçeneği kullanmak için ilgili numarayı girmeniz yeterlidir. Şifrelenmiş metinler `.protext` uzantılı dosyalarda saklanır.

## Örnek Kullanım

1. Metin şifreleme:
   - Seçenek 1'i seçin.
   - Bir başlık girin ve şifrelemek istediğiniz metni girin.
   - Şifrelenmiş metin belirtilen başlıkla kaydedilir.

2. Şifrelenmiş metni çözme:
   - Seçenek 2'yi seçin.
   - Şifrelenmiş metnin dosya adını girin.
   - Şifrelenmiş metin çözülür ve orijinal metin gösterilir.

## Güvenlik Uyarısı

Bu uygulama şifrelenmiş verilere erişim sağlayan bir ana şifre kullanır. Bu ana şifreyi kaybetmek, verilere erişiminizi kaybetmenize neden olabilir. Bu nedenle ana şifreyi güvenli bir şekilde saklamak önemlidir.
!!UYARI!! EĞİTİM İÇİN YAPILDI

!!WARNING!! MADE FOR EDUCATION

## İletişim

Sorularınız veya geri bildirimleriniz için [01Kevin0110@proton.me](mailto:01Kevin0110@proton.me) adresine e-posta gönderebilirsiniz.
Umarız bu kullanım talimatları, uygulamanın nasıl kullanılacağı konusunda size yardımcı olur. Daha fazla bilgi veya yardım için iletişim bilgilerinizi paylaşmayı unutmayın.
-------------------------------------------------------------------------------------------------------------------------------------------------
🇹🇷"Beni görmek demek mutlaka yüzümü görmek demek değildir. Benim fikirlerimi, benim duygularımı anlıyorsanız ve hissediyorsanız bu yeterlidir."🇹🇷
-Mustafa Kemal Atatürk

00110000 00110001 01001011 01100101 01110110 01101001 01101110 00110000 00110001 

"Siber güvenlik konusunda bilinçli olun ve saldırılar yerine, güvenliği arttırmak için çalışın."
#NewDayNewCyberSecurity
-------------------------------------------------------------------------------------------------------------------------------------------------
🇹🇷"Seeing me doesn't necessarily mean seeing my face. If you understand and feel my ideas and my feelings, that's enough."
-Mustafa Kemal Atatürk

00110000 00110001 01001011 01100101 01110110 01101001 01101110 00110000 00110001

"Be cybersecurity conscious and work to improve security rather than attacks."
#NewDayNewCyberSecurity
