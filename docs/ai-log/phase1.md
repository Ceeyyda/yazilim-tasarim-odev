\# AI Log: Phase 1 (Factory Method)



\### 1. AI'a Ne Sordunuz?

> "Mevcut bildirim sisteminde kullanıcı kayıt fonksiyonunun içinde EmailNotification ve PushNotification sınıfları if-else bloklarıyla doğrudan üretiliyor. Bu durum SOLID ilkelerine aykırı. Bu nesne üretim mantığını if-else karmaşasından kurtarmak ve bağımlılığı azaltmak için hangi yaratımsal örüntüyü, nasıl kullanabilirim? Python dilinde bir örnek verir misin?"



\### 2. AI Ne Yanıtladı? 

AI, nesne yaratma süreçlerini soyutlamak için \*\*Factory Method Pattern\*\* (Fabrika Örüntüsü) kullanmamı önerdi. Çözüm olarak; global bir fonksiyon veya basit bir fabrika yapısı üzerinden nesne türünü temsil eden string bir parametre alıp (`"email"`, `"push"`), ilgili nesneyi dönen bir kod taslağı paylaştı.



\### 3. Ben Ne Uyguladım ve Neden Farklı/Aynı?

AI'ın temel Fabrika mantığı önerisini aynen uyguladım. Ancak AI'ın kod taslağında sunduğu "global fonksiyon" yaklaşımını nesne yönelimli programlama prensiplerine tam olarak uygun bulmadığım için farklılaştırdım. 

Neden Farklı? Küresel fonksiyonlar nesne yönelimli mimaride kapsülleme (encapsulation) ilkesini zayıflatır. Bu yüzden üretimi `NotificationFactory` adında bağımsız, statik bir sınıf altına taşıdım. Ayrıca gelen string parametrelerdeki olası harf hatalarını önlemek için `.lower()` kontrolünü ekleyerek daha esnek ve kurumsal standartlara uygun bir mimari inşa ettim.

