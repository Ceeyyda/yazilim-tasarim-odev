from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Tüm bildirim sınıflarının uymak zorunda olduğu ortak arayüz.
    """

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


class SMSNotification(Notification):
    def __init__(self):
        self.sms_gateway = "https://api.sms-provider.com"

    def send(self, to, message, title=None, phone_number=None, device_token=None):
        if not phone_number:
            print("Hata: SMS için telefon numarası gerekli!")
            return False
        print(f"[{self.sms_gateway}] SMS gönderiliyor...")
        print(f"No: {phone_number}\nMesaj: {message}\n")
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


class NotificationFactory:
    """
    Nesne yaratma sorumluluğunu üstlenen fabrika sınıfımız.
    if-else zinciri buraya izole edilmiştir.
    """

    @staticmethod
    def create_notification(notification_type):
        target = notification_type.lower()
        if target == "email":
            return EmailNotification()
        elif target == "sms":
            return SMSNotification()
        elif target == "push":
            return PushNotification()
        else:
            raise ValueError(f"Hata: Desteklenmeyen bildirim tipi: {notification_type}")


if __name__ == "__main__":
    try:
        notifier = NotificationFactory.create_notification("email")
        notifier.send(to="ceyda@example.com", title="Tasarım Örüntüleri",
                      message="Factory Pattern başarıyla uygulandı!")

        sms_notifier = NotificationFactory.create_notification("sms")
        sms_notifier.send(to=None, message="Kodunuz: 1923", phone_number="+90555...")

    except ValueError as e:
        print(e)