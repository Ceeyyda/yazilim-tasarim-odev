\# Tasarım Örüntüleri Dönem Ödevi: Bildirim Sistemi (A Şıkkı)



\## 📌 Proje Seçim Gerekçesi

Günümüz modern yazılım mimarilerinde e-posta, SMS ve anlık bildirimlerin esnek, modüler ve gevşek bağımlı bir yapıda yönetilmesi sistem sağlığı açısından kritik bir öneme sahiptir. 



Bu projede; tüm bildirim tiplerinin tek bir dev sınıfta (God Class) toplandığı, SOLID ilkelerini ağır şekilde ihlal eden ve spagetti `if-else` zincirleriyle yönetilen kötü bir tasarımı ele aldım. Bu hatalı başlangıç mimarisini nesne yönelimli programlama prensipleriyle adım adım iyileştirerek;

1\. \*\*Factory Method (Yaratımsal):\*\* Nesne üretim süreçlerini izole etmek,

2\. \*\*Adapter (Yapısal):\*\* Uyumsuz üçüncü parti dış kütüphaneleri sisteme entegre etmek,

3\. \*\*Observer (Davranışsal):\*\* Olay-güdümlü dinamik bir bildirim tetikleme altyapısı kurmak



amacıyla ve bu örüntülerin kodun sürdürülebilirliğine olan doğrudan etkisini deneyimlemek için \*\*A şıkkını\*\* seçtim.



\---



\## 🛠️ Proje Klasör Yapısı

\* `src/main.py`: Tüm tasarım örüntülerinin (Factory, Adapter, Observer) uygulandığı nihai kaynak kod.

\* `PROBLEMS.md`: Faz 0 aşamasında spagetti kod üzerinde yapılan mimari zafiyet analizi.

\* `PATTERNS.md`: Projede uygulanan tüm tasarım örüntülerinin gerekçeli raporu.

\* `docs/ai-log/`: Yapay zeka ile yapılan mimari tartışmaların ve refleksiyonların aşama aşama tutulan günlükleri.

## 📊 Sistem Mimari Diyagramı
![Sistem Tasarım Diyagramı](design-diagram.png)