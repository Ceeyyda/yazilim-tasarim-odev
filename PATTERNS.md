1. Örüntü Seçim Gerekçesi
Faz 0 aşamasındaki en büyük sorunlardan biri, bildirim nesnelerinin (EmailNotification, PushNotification) istemci kodunun içinde doğrudan new anahtar kelimesiyle (veya Python'da doğrudan sınıf çağrısıyla) üretilmesiydi. Bu durum sisteme yeni bir bildirim türü eklendiğinde ana kod yapısının bozulmasına yol açıyordu. İstemciyi nesne yaratma detaylarından soyutlamak ve nesne üretim mantığını tek bir merkezde toplamak amacıyla Factory Method Pattern seçtim.

2. Uygulama Detayları
Notification adında soyut bir temel sınıf oluşturuldu ve tüm bildirim türlerinin bu sınıftan türemesi sağlandı.

Nesne üretim sorumluluğu istemciden alınarak statik bir NotificationFactory sınıfına devredildi.

Fabrika sınıfı içerisindeki create_notification(notification_type) metodu, gelen parametreye göre ("email", "push") arka planda doğru nesneyi inşa edip istemciye polimorfik (çok biçimli) olarak geri döndürmektedir.

3. Kod Kalitesine Etkisi Gevşek Bağımlılık (Loose Coupling): İstemci artık hangi somut bildirim sınıfının çalıştığını bilmek zorunda değildir; sadece Notification arayüzü ile konuşur.

Open-Closed Principle Uyumu: İleride sisteme yeni bir bildirim türü (örneğin SMS veya Slack) dahil etmek istediğimizde istemci koduna dokunmadan, sadece fabrikayı genişleterek bu entegrasyonu sağlayabiliriz.

Kod Tekrarının Önlenmesi: Nesnelerin yapılandırılma mantığı tek bir merkezde toplandığı için kodun bakımı ve yönetimi kolaylaşmıştır.

4. Yapay Zekanın Çözümüne Eleştirel Yaklaşım ve Mühendislik Yorumu
AI Önerisi: Yapay zeka, nesne üretim sürecini doğrudan global bir fonksiyon halinde veya ana kayıt fonksiyonunun hemen üstünde basit bir if-else yapısı olarak tasarlamayı önerdi.

Eleştiri ve Değişikliklerim: Bir yazılım mühendisi adayı olarak AI'ın bu yaklaşımının nesne yönelimli programlama (OOP) kültürüne tam uymadığını ve "Encapsulation" (Kapsülleme) ilkesini zayıflattığını fark ettim. AI'ın önerdiği dağınık yapıyı reddederek, üretimi tamamen kurumsal standartlara uygun, bağımsız bir NotificationFactory sınıfı altında topladım. Parametre kontrollerini (örneğin büyük/küçük harf duyarlılığını ortadan kaldırmak için .lower() dönüşümünü) fabrika içine gömerek istemcinin hata yapma ihtimalini sıfıra indirdim. Bu sayede AI'ın önerdiğinden çok daha modüler ve kurallara sadık bir mimari ortaya çıkardım.

## 2. Adapter Pattern (Yapısal Örüntü)
Projeyi geliştirirken Faz 2 aşamasında en çok zorlandığım yer, dışarıdan aldığımız YurtIciSmsProvider kütüphanesinin parametre yapısı oldu. Bizim sistemimiz send(to, message...) şeklinde standart bir yapıda çalışırken, bu hazır kütüphane gonder_sms_mesaji(tel_no, metin_icerigi) gibi tamamen Türkçe ve farklı sırada parametreler istiyordu. Eğer Adapter Pattern kullanmasaydım, ana fabrikadaki tüm if-else yapılarını ve istemci kodlarını bu kütüphaneye göre baştan aşağı değiştirmem gerekecekti. Yazdığım YurtIciSmsAdapter sınıfı sayesinde, dış kütüphaneyi adeta bir yapboz parçası gibi sisteme uydurdum. Bu bana yazılımda 'Açık/Kapalı Prensibi'nin (OCP) ne kadar hayat kurtarıcı olduğunu bizzat deneyimletti.

## 3. Observer Pattern (Davranışsal Örüntü)
* **Nerede Kullanıldı:** `src/main.py` içerisindeki `UserRegistry` (Subject) ve `Notification` (Observer) yapılarında kullanıldı.
* **Neden Seçildi:** Kullanıcı kayıt olayı gibi sistem tetiklemelerinde, bildirim modüllerini ana sisteme sıkı sıkıya bağlamadan (de-coupling) dinamik bir haberleşme ağı kurmak için seçildi.
* **Ne Kazandırdı:** Sisteme gelecekte yeni bir bildirim kanalı (örneğin TelegramNotification) eklendiğinde, `UserRegistry` sınıfının kaynak koduna tek bir satır dahi dokunmadan, sadece `attach()` metoduyla sisteme canlı olarak bağlanabilmesi yeteneğini kazandırdı.