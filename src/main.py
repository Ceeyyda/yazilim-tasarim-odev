from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, to, message, title=None, phone_number=None, device_token=None):
        pass


class EmailNotification(Notification):
    def __init__(self):
        self.smtp_server = "smtp.company.com"

    def send(self, to, message, title=None, phone_number=None, device_token=None):
        if not to or "@" not in to:
            print("Hata: Geçersiz e-posta adresi!")
            return False
        print(f"[{self.smtp_server}] E-posta gönderiliyor...")
        print(f"Kime: {to}\nKonu: {title}\nMesaj: {message}\n")
        return True


class PushNotification(Notification):
    def __init__(self):
        self.push_firebase_key = "fb-xyz-123"

    def send(self, to, message, title=None, phone_number=None, device_token=None):
        if not device_token:
            print("Hata: Push bildirim için cihaz token'ı gerekli!")
            return False
        print(f"[{self.push_firebase_key}] Push bildirim tetiklendi...")
        print(f"Token: {device_token}\nBaşlık: {title}\nİçerik: {message}\n")
        return True

class YurtIciSmsProvider:
    """
    Bu sınıf dışarıdan hazır aldığımız, kaynak kodunu değiştiremediğimiz
    ve bizim mevcut Notification arayüzümüze tamamen uyumsuz olan sınıftır.
    """

    def __init__(self):
        self.api_key = "YURTICI-SMS-9988"

    def gonder_sms_mesaji(self, tel_no, metin_icerigi):
        if not tel_no.startswith("+90"):
            print("Hata: Yurtİçi SMS sadece Türkiye numaralarına gönderim yapabilir!")
            return False
        print(f"[{self.api_key}] Yurtİçi SMS Sağlayıcısı Çalıştı.")
        print(f"Alıcı: {tel_no}\nSMS Metni: {metin_icerigi}\n")
        return True


class YurtIciSmsAdapter(Notification):
    """
    Uyumsuz YurtIciSmsProvider sınıfını, bizim Notification arayüzümüze
    uyumlu hale getiren köprü (Adaptör) sınıfımız.
    """

    def __init__(self):
        # Uyumsuz nesneyi kendi içine sarıyor (Composition / Sarmalama)
        self.adaptee = YurtIciSmsProvider()

    def send(self, to, message, title=None, phone_number=None, device_token=None):
        # Bizim standart 'send' çağrımızı, dış kütüphanenin anladığı dile tercüme ediyor
        if not phone_number:
            print("Hata: Adaptör - Telefon numarası eksik!")
            return False

        success = self.adaptee.gonder_sms_mesaji(tel_no=phone_number, metin_icerigi=message)
        return success


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        target = notification_type.lower()
        if target == "email":
            return EmailNotification()
        elif target == "push":
            return PushNotification()
        elif target == "sms":
            return YurtIciSmsAdapter()
        else:
            raise ValueError(f"Hata: Desteklenmeyen bildirim tipi: {notification_type}")


if __name__ == "__main__":
    try:
        print("--- Standart Email Gönderimi (Faz 1) ---")
        email_notifier = NotificationFactory.create_notification("email")
        email_notifier.send(to="ceyda@example.com", title="Dönem Ödevi", message="Sistem evrimleşiyor.")

        print("--- Adaptör Üzerinden Yeni Yurtİçi SMS Gönderimi (Faz 2) ---")
        # İstemci eski 'sms' anahtar kelimesiyle ve standart 'send' metoduyla çağrı yapıyor
        sms_notifier = NotificationFactory.create_notification("sms")
        sms_notifier.send(to=None, message="Sisteme başarıyla adapte edildim!", phone_number="+905321112233")

    except ValueError as e:
        print(e)