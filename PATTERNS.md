\# Uygulanan Tasarım Örüntüleri



\## 1. Factory Method (Yaratımsal Örüntü)

\* \*\*Nerede Kullanıldı:\*\* `src/main.py` içerisindeki `NotificationFactory` sınıfında nesne üretim süreçlerinde kullanıldı.

\* \*\*Neden Seçildi:\*\* İstemci tarafını (`main`) hangi somut bildirim nesnesinin (Email, SMS vb.) üretileceği detayından kurtarmak ve if-else kontrolünü tek bir noktaya hapsetmek için seçildi.

\* \*\*Ne Kazandırdı:\*\* Yeni bir bildirim türü eklendiğinde istemci kodu veya diğer bildirim sınıfları bundan etkilenmeyecek. Kod esneklik kazandı.

