\# Faz 0: Başlangıç Kodu Tasarım Analiz Raporu



Bu raporda, `src/main.py` dosyasındaki mevcut bildirim sistemi mimarisinin nesne yönelimli programlama (OOP) ve SOLID prensipleri açısından barındırdığı temel tasarım hataları listelenmiştir.



\## Tespit Edilen Tasarım Sorunları



\### 1. Tek Sorumluluk Prensibi (Single Responsibility Principle - SRP) İhlali

\* \*\*Sorun:\*\* `NotificationService` sınıfı hem e-posta, hem SMS, hem de push bildirimlerinin iş mantığını, doğrulama kurallarunı ve bağlantı bilgilerini tek başına barındırmaktadır.

\* \*\*Neden Sorun?:\*\* Sınıfın değişmesi için birden fazla neden vardır; bu durum kodun sürdürülebilirliğini ve okunabilirliğini ciddi şekilde düşürür.



\### 2. Açık/Kapalı Prensibi (Open/Closed Principle - OCP) İhlali

\* \*\*Sorun:\*\* Yeni bir bildirim türü (örneğin WhatsApp) eklenmek istendiğinde, `send\_notification` metodunun içine yeni `elif` blokları eklenmesi gerekmektedir.

\* \*\*Neden Sorun?:\*\* Mevcut ve çalışan bir koda sürekli müdahale etmek, sistemi genişletmeye kapalı hale getirir ve eski çalışan özellikleri kırma riskini artırır.



\### 3. Sıkı Bağımlılık (Tight Coupling) ve Esneklik Eksikliği

\* \*\*Sorun:\*\* E-posta, SMS ve push servislerine ait konfigürasyonlar `NotificationService` constructor'ı (`\_\_init\_\_`) içerisinde sabit olarak kodlanmıştır.

\* \*\*Neden Sorun?:\*\* Çalışma zamanında (runtime) farklı bir SMS sağlayıcısına geçiş yapmayı imkansız kılar.



\### 4. Metot Parametre Enflasyonu (Code Smell)

\* \*\*Sorun:\*\* `send\_notification` metodu; `to`, `phone\_number`, `device\_token` gibi tüm bildirim tiplerine ait parametreleri tek bir imzada toplamak zorunda kalmıştır.

\* \*\*Neden Sorun?:\*\* Kullanıcı SMS göndermek istediğinde e-posta parametrelerini `None` geçmek zorundadır.



\### 5. Koşullu Mantık Zincirleri (İf-Else Bağımlılığı)

\* \*\*Sorun:\*\* Bildirim türünün ayrımı, metot içerisindeki string tabanlı `if-else` koşul zincirleriyle sağlanmaktadır.

\* \*\*Neden Sorun?:\*\* String ifadeler yazım hatalarına açıktır ve polymorphism (çok biçimlilik) yerine usulsel if-else bloklarına sığınmak nesne felsefesine aykırıdır.



\---



\## 🤖 Yapay Zeka (AI) Karşılaştırma Raporu



\* \*\*AI Tarafından Görülüp Benim Gördüklerimle Eşleşenler:\*\* Nesne yaratma süreçlerinin soyutlanmaması, if-else zincirlerinin esnekliği bozması ve SOLID (SRP/OCP) ilkelerinin ağır ihlali ortak olarak vurgulanmıştır.

\* \*\*Farklar / Ekstra Tespitler:\*\* Yapay zeka, hata yönetiminin (try-except) eksikliğini ek bir mimari zafiyet olarak belirtmiştir. Nesne üretim sorumluluğunun merkezi bir "Creational" örüntüye taşınması gerektiği ortak karardır.

