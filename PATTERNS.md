# Uygulanan Tasarım Örüntüleri

## 1. Factory Method (Yaratımsal Örüntü)
* **Nerede Kullanıldı:** `src/main.py` içerisindeki `NotificationFactory` sınıfında nesne üretim süreçlerinde kullanıldı.
* **Neden Seçildi:** İstemci tarafını (`main`) hangi somut bildirim nesnesinin (Email, SMS vb.) üretileceği detayından kurtarmak ve if-else kontrolünü tek bir noktaya hapsetmek için seçildi.
* **Ne Kazandırdı:** Yeni bir bildirim türü eklendiğinde istemci kodu veya diğer bildirim sınıfları bundan etkilenmeyecek. Kod esneklik kazandı.

## 2. Adapter Pattern (Yapısal Örüntü)
Projeyi geliştirirken Faz 2 aşamasında en çok zorlandığım yer, dışarıdan aldığımız YurtIciSmsProvider kütüphanesinin parametre yapısı oldu. Bizim sistemimiz send(to, message...) şeklinde standart bir yapıda çalışırken, bu hazır kütüphane gonder_sms_mesaji(tel_no, metin_icerigi) gibi tamamen Türkçe ve farklı sırada parametreler istiyordu. Eğer Adapter Pattern kullanmasaydım, ana fabrikadaki tüm if-else yapılarını ve istemci kodlarını bu kütüphaneye göre baştan aşağı değiştirmem gerekecekti. Yazdığım YurtIciSmsAdapter sınıfı sayesinde, dış kütüphaneyi adeta bir yapboz parçası gibi sisteme uydurdum. Bu bana yazılımda 'Açık/Kapalı Prensibi'nin (OCP) ne kadar hayat kurtarıcı olduğunu bizzat deneyimletti.

## 3. Observer Pattern (Davranışsal Örüntü)
* **Nerede Kullanıldı:** `src/main.py` içerisindeki `UserRegistry` (Subject) ve `Notification` (Observer) yapılarında kullanıldı.
* **Neden Seçildi:** Kullanıcı kayıt olayı gibi sistem tetiklemelerinde, bildirim modüllerini ana sisteme sıkı sıkıya bağlamadan (de-coupling) dinamik bir haberleşme ağı kurmak için seçildi.
* **Ne Kazandırdı:** Sisteme gelecekte yeni bir bildirim kanalı (örneğin TelegramNotification) eklendiğinde, `UserRegistry` sınıfının kaynak koduna tek bir satır dahi dokunmadan, sadece `attach()` metoduyla sisteme canlı olarak bağlanabilmesi yeteneğini kazandırdı.