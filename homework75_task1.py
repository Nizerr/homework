class NotificationService:
    def __init__(self):
        self.notification_methods = []

    def add_notification_method(self, notification_method):
        self.notification_methods.append(notification_method)

    def send_notification(self, message, receiver):
        for method in self.notification_methods:
            method.send(message, receiver)

class EmailService:
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SMSService:
    def send(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")


email_service = EmailService()
sms_service = SMSService()

notification_service = NotificationService()
notification_service.add_notification_method(email_service)
notification_service.add_notification_method(sms_service)

notification_service.send_notification("Привіт", "rostyslav@gmail.com")
notification_service.send_notification("Зробіть замовлення на нашому стайті", "+380837751")