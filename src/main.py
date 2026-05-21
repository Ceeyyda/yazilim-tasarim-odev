from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Sistemdeki olayları (Event) dinleyecek olan gözlemci arayüzü.
    """
    @abstractmethod
    def update(self, user_name, email, phone_number):
        pass


class Notification(ABC, Observer):
    """
    Notification artık hem bir bildirim arayüzü hem de bir Observer'dır.
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

    def update(self, user_name, email, phone_number):
        self.send(to=email, title="Sisteme Hoş Geldiniz!", message=f"Merhaba {user_name}, kaydınız onaylandı.")


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

    def update(self, user_name, email, phone_number):
        pass


class YurtIciSmsProvider:
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
    def __init__(self):
        self.adaptee = YurtIciSmsProvider()

    def send(self, to, message, title=None, phone_number=None, device_token=None):
        if not phone_number:
            print("Hata: Adaptör - Telefon numarası eksik!")
            return False
        return self.adaptee.gonder_sms_mesaji(tel_no=phone_number, metin_icerigi=message)

    def update(self, user_name, email, phone_number):
        self.send(to=None, message=f"Sayın {user_name}, aktivasyon kodunuz: 7200", phone_number=phone_number)


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


class UserRegistry:
    """
    Kullanıcı kayıt işlemlerini yürüten ve bir olay gerçekleştiğinde
    gözlemcilere (Observers) haber veren 'Subject' sınıfımız.
    """
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, user_name, email, phone_number):
        for observer in self._observers:
            observer.update(user_name, email, phone_number)

    def register_user(self, user_name, email, phone_number):
        print(f"\n[SİSTEM] Yeni kullanıcı veritabanına kaydedildi: {user_name}")
        self.notify_observers(user_name, email, phone_number)


if __name__ == "__main__":
    system_registry = UserRegistry()

    email_service = NotificationFactory.create_notification("email")
    sms_service = NotificationFactory.create_notification("sms")

    system_registry.attach(email_service)
    system_registry.attach(sms_service)

    system_registry.register_user(
        user_name="Ceyda Ardıç",
        email="ceyda@example.com",
        phone_number="+905551234567"
    )