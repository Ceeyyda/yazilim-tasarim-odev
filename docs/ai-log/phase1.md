\# Faz 1 - AI Log Raporu



\* \*\*AI'a ne soruldu (Prompt):\*\* "Koddaki if-else bağımlılığını ve nesne üretim karmaşasını çözmek için hangi Creational örüntü uygundur? Nesne üretim sorumluluğunu God Class'tan nasıl ayırırız?"

\* \*\*AI ne yanıtladı (Özet):\*\* AI, tüm bildirim tiplerinin ortak bir soyut sınıftan (Interface/Abstract) türetilmesini ve nesne üretim sürecinin 'Factory Method' örüntüsüyle bir fabrika sınıfına devredilmesini önerdi.

\* \*\*Ben ne uyguladım ve neden:\*\* AI'ın önerisine sadık kalarak `Notification` taban sınıfını ve `NotificationFactory` yapısını kurdum. Kodun genişletilebilirliği arttı.

