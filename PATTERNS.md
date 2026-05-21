# Uygulanan Tasarım Örüntüleri

## 1. Factory Method (Yaratımsal Örüntü)
* **Nerede Kullanıldı:** `src/main.py` içerisindeki `NotificationFactory` sınıfında nesne üretim süreçlerinde kullanıldı.
* **Neden Seçildi:** İstemci tarafını (`main`) hangi somut bildirim nesnesinin (Email, SMS vb.) üretileceği detayından kurtarmak ve if-else kontrolünü tek bir noktaya hapsetmek için seçildi.
* **Ne Kazandırdı:** Yeni bir bildirim türü eklendiğinde istemci kodu veya diğer bildirim sınıfları bundan etkilenmeyecek. Kod esneklik kazandı.

## 2. Adapter Pattern (Yapısal Örüntü)
* **Nerede Kullanıldı:** `src/main.py` içerisine eklenen `YurtIciSmsAdapter` sınıfında kullanıldı.
* **Neden Seçildi:** Sisteme sonradan dahil olan uyumsuz ve değiştirilemez `YurtIciSmsProvider` kütüphanesini, mevcut `Notification` arayüzümüze entegre etmek için seçildi.
* **Ne Kazandırdı:** Açık/Kapalı prensibine (OCP) sadık kalındı; fabrikadaki tek bir satır hariç hiçbir çalışan eski koda dokunulmadan sisteme yeni ve güçlü bir yapı kazandırıldı.

## 3. Observer Pattern (Davranışsal Örüntü)
* **Nerede Kullanıldı:** `src/main.py` içerisindeki `UserRegistry` (Subject) ve `Notification` (Observer) yapılarında kullanıldı.
* **Neden Seçildi:** Kullanıcı kayıt olayı gibi sistem tetiklemelerinde, bildirim modüllerini ana sisteme sıkı sıkıya bağlamadan (de-coupling) dinamik bir haberleşme ağı kurmak için seçildi.
* **Ne Kazandırdı:** Sisteme gelecekte yeni bir bildirim kanalı (örneğin TelegramNotification) eklendiğinde, `UserRegistry` sınıfının kaynak koduna tek bir satır dahi dokunmadan, sadece `attach()` metoduyla sisteme canlı olarak bağlanabilmesi yeteneğini kazandırdı.