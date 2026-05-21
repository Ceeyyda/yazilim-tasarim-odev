\# AI Log: Phase 2 (Adapter Pattern)



\### 1. AI'a Sorulan Soru (Prompt)

> "Sisteme entegre etmek istediğim üçüncü parti bir Türkçe SMS kütüphanesi var (YurtIciSmsProvider). Ancak fonksiyon ve parametre isimleri mevcut bildirim arayüzümle tamamen uyumsuz. Bu uyumsuzluk sorununu çözmek için Adapter pattern burada uygun mu, yoksa Facade mi kullanmalıyım? İki örüntünün farkını açıklayarak projem için bir seçim yapar mısın?"



\### 2. AI Ne Yanıtladı? (Özet)

AI, her iki örüntünün de yapısal (structural) örüntüler olduğunu ancak amaçlarının tamamen farklı olduğunu belirtti:

\* \*\*Adapter:\*\* Uyumsuz bir arayüzü, mevcut sistemin beklediği başka bir arayüze dönüştürür (Arayüz çeviricidir).

\* \*\*Facade:\*\* Karmaşık ve çok sayıda alt sistemden oluşan bir yapıyı, tek bir basitleştirilmiş üst sınıf arkasına gizler (Arayüz basitleştiricidir).

Projede tek bir üçüncü parti sınıfın arayüz uyumsuzluğu çözülmek istendiği için AI, kesinlikle \*\*Adapter Pattern\*\* kullanılmasını önerdi.



\### 3. AI'ın Yanlış veya Eksik Önerdiği Bir Şey Bulundu mu? 

\*\*Evet, buldum.\*\* AI, adaptör sınıfını yazarken çok temel bir nesne yönelimli tasarım hatası yaptı. `YurtIciSmsAdapter` sınıfını tasarlarken, dış kütüphaneyi (`YurtIciSmsProvider`) sınıf düzeyinde kalıtım (Inheritance / Class Adapter) yoluyla bağlamayı önerdi.

\* \*\*Eleştiri ve Değişikliğim:\*\* Sınıf düzeyinde kalıtım kullanmak, bizim sistemimizi o dış kütüphaneye çok sıkı bağlar (tight coupling). Yazılım mühendisliğinde \*"Composition over Inheritance"\* (Kalıtım yerine Kompozisyon/Sarmalama kullanımı) ilkesi esastır. AI'ın bu eksikliğini fark ederek öneriyi reddettim. Sınıf kalıtımı yerine, dış kütüphane nesnesini adaptör sınıfının içinde bir üye değişken olarak sarmaladım (\*\*Object Adapter\*\* yaklaşımı). Böylece kütüphaneyi sistemimize tamamen gevşek bağlı (loose coupled) hale getirdim.



\### 4. Belgeleme ve Mimari Tercih Nedeni

Projemizde karmaşık bir kütüphane alt sistemini basitleştirmek gibi bir ihtiyacımız olmadığı, sadece mevcut `Notification.send()` sözleşmesine uyumsuz bir dış fonksiyonu adapte etmek istediğimiz için \*\*Facade elenmiş, Adapter Pattern mimariye başarıyla işlenmiştir.\*\*

