class NotificationService:
    def __init__(self):
        # Gerçek hayatta burası bağlantı bilgileri ile dolar ve şişer
        self.smtp_server = "smtp.company.com"
        self.sms_gateway = "https://api.sms-provider.com"
        self.push_firebase_key = "fb-xyz-123"

    def send_notification(self, notification_type, to, message, title=None, phone_number=None, device_token=None):
        """
        Tüm bildirim tipleri tek bir sınıfta. if-else zincirleri ile tip kontrolü yapılıyor.
        """
        if notification_type.lower() == "email":
            if not to or "@" not in to:
                print("Hata: Geçersiz e-posta adresi!")
                return False
            print(f"[{self.smtp_server}] E-posta gönderiliyor...")
            print(f"Kime: {to}\nKonu: {title}\nMesaj: {message}\n")
            return True

        elif notification_type.lower() == "sms":
            if not phone_number:
                print("Hata: SMS için telefon numarası gerekli!")
                return False
            print(f"[{self.sms_gateway}] SMS gönderiliyor...")
            print(f"No: {phone_number}\nMesaj: {message}\n")
            return True

        elif notification_type.lower() == "push":
            if not device_token:
                print("Hata: Push bildirim için cihaz token'ı gerekli!")
                return False
            print(f"[{self.push_firebase_key}] Push bildirim tetiklendi...")
            print(f"Token: {device_token}\nBaşlık: {title}\nİçerik: {message}\n")
            return True

        else:
            print(f"Hata: Desteklenmeyen bildirim tipi: {notification_type}")
            return False


if __name__ == "__main__":
    service = NotificationService()
    service.send_notification("email", to="ceyda@example.com", title="Ödev Başladı", message="Faz 0 aşamasındayız.")