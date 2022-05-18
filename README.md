
# TeleLiman
Uygulama Liman MYS kullanıcılarının telefon üzerinden hızlı bir şekilde daha öncesinde yapılandırılmış serverlarına hızlı ve basit bir erişim sağlayan PHP ve Python ile yazılmış bir eklentidir.
## Bu uygulama nelere yardımcı olur?
Sistem yöneticilerinin işlerini kolaylaştırmak amacıyla yazılmıştır. 

**Uygulama:**
1. Önceden eklentinin eklediği servislerde update, reboot, shutdown methodlarının uygulama üzerinde çalışması
2. Eklenmiş olan servislerin start, stop ve status işlemlerinin yapılmasını sağlaması
3. Herhangi bir çökme durumunda sorunun anında Sistem Yöneticisine bildirilmesi
**Odaklanılmıştır.**

**Geliştirici Notu**
> Uygulama hızlı bir şekilde geliştirildiğinden dolayı sorunların tespiti konusunda daha fazla düşünülebilir. Geliştirilen dizayn yapısı hızlı bir şekilde geliştirilmeye müsaittir. 

## Uygulamanın avantajları nelerdir?
Kullanılan sistemlerin telefon erişimi sayesinde hızlıca görüntülenebilmesi, plugin üzerinde ufak değişikliklerle her ihtiyaca uygun bir bot tasarlanabilmesini sağlar.

**Örnek vermemiz gerekirse:**

1. Uygulama bir helper sayesinde kullanıcıdan gelen istekler doğrultusunda betikler çalıştırır. Betiklerin oluşturulabilmesi ve bot üzerine eklenebilmesi oldukça basittir.
2. Telegram üzerinden çıkış sağlandığından dolayı uygulama üzerine gönderilebilecek istekler başka bir güvenlik üzerinden daha geçer bu sayede uygulamaya ekstra güvenlik sağlar. (Güvenlik konusuna "Geliştiriciler için" kısmında daha detaylı değinilecektir.)
3. Sunucuların bakımların kişilere TeleLiman uygulaması üzerinden rahatlıkla dağıtılabilmesini sağlar.

# Kurulum
Bu kısımda eklentinin nasıl doğru bir şekilde yapılandırılıp kurulabileceğine ayrıntılı şekilde girilecektir.
## Telegram Botunun oluşturulması
1. Telegram üzerinden '@BotFather' botu bulunur. Bu bota /start komutu verilerek bot kullanılmaya başlanır.
2. /newbot komutu kullanılır. İlk aşamada bota bir isim verilir. Bu isim kullanıcı adı değil botun ismidir.
3. Sonrasında bota benzersiz bir kullanıcı adı seçilmelidir. Bota seçilen kullanıcı adı '*Bot' veya '*_bot' yapısına uygun olarak belirlenmelidir. Örneğin 'test123a_bot' 'test123aBot' gibi...
4. Sonrasında @BotFather bize http API token'ımızı verir. Bu token uygulamanın diğer aşamalarında bize yardımcı olacaktır bu yüzden not almanız önerilir.

## Otomatik kurulum
1.  [install.sh](https://teleliman.github.io/download/install.sh "install.sh") dosyası sunucu üzerine indirilir ve çalıştırılır.
>  wget https://teleliman.github.io/download/install.sh 
./install.sh

2.  Liman MYS arayüzü üzerine giriş yapılarak ilgili sunucuya ilgili eklenti eklenir. [Liman MYS eklenti kurulum dokumanı](https://docs.liman.dev/kullanim-kilavuzu/liman-kurulumu/eklenti-kurulumu-ve-guencellemeler "Liman MYS eklenti kurulum dokumanı")
3.  Yan panelden ilgili sunucu seçilerek sunucunun altındaki panelde bulunan telegram uygulaması seçilir. Gelen ekrandan telegram_token, telegram_username ve yönetilmek istenen sunucunun root şifresi girilir.
4.  Sonra yan panelde bulunan eklenti ismine tıklanır. Ekranda bulunan 'Konfigure et' butonuna tıklanmasının ardından ilgili sunucu yeniden başlatılır.

## Manuel Kurulum


1.  Sunucu üzerindeki bekleyen güncelleştirmeler yapılır.

	> sudo apt update & sudo apt upgrade -y

2.  Gerekli uygulamaların kurulması

	> sudo apt install python3, python3-pip, git, wget, python3-paramiko
	 pip3 install requests, json

3.  Eklenti dosyalarının sunucu üzerine indirilmesi

	>  git clone https://github.com/TeleLiman/TelelimanExtension.git /liman/extensions 
	 mv TelelimanExtension/ teleliman/

4.  Servis komutlarının girilmesi

	>  echo 'nohup python3 /liman/extensions/teleliman/scripts/main.py > /dev/null 2>&1 &' > /root/service.sh
	 wget -P /etc/systemd/system/ https://teleliman.github.io/download/teleliman.service
	 systemctl daemon-reload 
	 systemctl enable teleliman.service 
	 systemctl start teleliman.service

5.  Liman MYS arayüzü üzerine giriş yapılarak ilgili sunucuya ilgili eklenti eklenir. [Liman MYS eklenti kurulum dokumanı](https://docs.liman.dev/kullanim-kilavuzu/liman-kurulumu/eklenti-kurulumu-ve-guencellemeler "Liman MYS eklenti kurulum dokumanı")
6.  Yan panelden ilgili sunucu seçilerek sunucunun altındaki panelde bulunan telegram uygulaması seçilir. Gelen ekrandan telegram_token, telegram_username ve yönetilmek istenen sunucunun root şifresi girilir.

7.  Sonra yan panelde bulunan eklenti ismine tıklanır. Ekranda bulunan 'Konfigure et' butonuna tıklanmasının ardından ilgili sunucu yeniden başlatılır.


# Kullanım
Bu kısımda ilgili servislerin nasıl kullanılabileceğine değinilmiştir. Servis yapısı gereği geliştirilmeye açıktır. Aşağıda eklenen komutlar örnek olarak tasarlanmıştır.

## Fonksiyonlar
**/shutdown**: İlgili sunucunun kapatılmasını sağlar.

**/reboot**: İlgili sunucunun yeniden başlatılmasını sağlar.

**/update**: İlgili sunucunun güncellenmesini sağlar.

**/startservice**: İlgili sunucudaki bir servisinin başlatılmasını sağlar.

**/stopservice**: İlgili sunucudaki bir servisinin kapatılmasını sağlar.

**/statusservice**: İlgili sunucudaki bir servisinin durumunun sorgulanmasını sağlar.

**/uname**: İlgili sunucunun uname fonksiyonun çalıştırılmasını sağlar.

## Çökme Raporu
Herhangi bir sunucunda çökme durumu oluştuğunda uygulama otomatik olarak app üzerinden mesaj gönderir.

# Geliştiriciler İçin
Bu kısımda uygulamanın yapısı anlatılacaktır. Yazılan eklentiyi manipüle ederek kendi fonksiyonlarınızı ekleyebilir istekleriniz doğrultusunda geliştirebilirsiniz.

## Dosya Yapısı
Liman MYS'nin belirttiği dosya yapısı aktif olarak kullanılmaktadır. [LimanMYS dosya yapısı](https://docs.liman.dev/eklenti-gelistirme/genel-bilgiler/dizin-yapisi "LimanMYS dosya yapısı") Artı olarak /root/service.sh isminde başlangıç servisimiz mevcuttur.

## Çalışma Mantığı
Liman MYS üzerinden server() ve extensionDb() ile Liman MYS üzerinden alınan bilgiler scripts/settings.json dosyası içine işlenir. scripts/main.py dosyası json içindeki verileri kullanarak uzak sunuculara ssh yardımıyla bağlanır. Telegramdan gelen istekleri bu uzak sunucu üzerinde gerçekleştirir.

## Helpers
1.   Telegram üzerinde bulunan sendMessage() fonksiyonu, helpers içine eklenmiş ve böylece tüm uygulama çıktıları mesaj iletebilme özelliğine sahip olmuştur (Bkz. scripts/Helpers.py)
2.   Telegram üzerinde bulunan getUpdates() fonksiyonu, helpers içine eklenmiş ve böylece tüm uygulama telegram üzerinden veri okuma özelliğine sahip olmuştur (Bkz. scripts/Helpers.py)

# Gelecek Sürümler
Bu uygulama Havelsan Express Liman MYS Fikir Yarışması süresince geliştirilmiştir. Liman MYS Core'a herhangi bir müdahale edilmeden tasarlanmıştır. Aşağıda geliştirilebilecek uygulamayı daha ileriye taşıyacak fikirler developerlar ve juri için yazılmıştır.


**1.  İki adımlı kimlik doğrulama (2fa):** Uygulamayı ilk defa kurduğumuzda en çok ilgimizi çeken uygulama üzerinde herhangi bir authentication faktörünün bulunmamasıydı. Core'a müdahale edemediğimizden dolayı herhangi bir authentication eklemedik.

**2.     Kullanıcı Engelleme:** İçerde zararlı bir kullanıcı tespit edildiğinde otomatik olarak sistem tarafından banlanır.

**3.     Liman MYS Sürüm Kontroli:** Liman MYS üzerinde sürüm değişikliği olduğunda Telegram üzerinden sunucu yöneticisine izin verilebilir. Core müdehalesi yasak olduğundan ve uygulama bize böyle bir arayüz sunmadığından gerçekleştirilemedi.

**4.     Tek Bot Çoklu Sunucu:** Her sunucu için farklı bot oluşturmak yerine işlem yapılacak sunucu seçilerek işlem yaptırılabilinir.

**5.     Whitelist İp Bloğuna Ekleme:** İstenirse sisteme yanlızca belirli iplerden giriş sağlanabilir. Eğer yeni bir ip adresi eklenecekse bu işlem TeleLiman üzerinde yürütülebilir.

**6.     Pardus Liman Edition:** Liman kurulu sunucularda başka hiçbir işlem yapılmayacağı varsayıldığından limanın yüklü olarak geldiği bir .iso paketi hazırlanabilir.

