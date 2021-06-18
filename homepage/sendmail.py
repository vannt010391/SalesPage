from django.core.mail import send_mail
import uuid
from django.conf import settings
def send_forget_password_mail(email,token):
    token = token
    subject = 'Đổi mật khẩu Salepage    '
    message = f"Chào bạn, Bấm vào đường link dưới đây để thay đổi mật khẩu của bạn http://127.0.0.1:8000/ResetPassConfirmForm"
    email_form = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject, message,email_form,recipient_list)
    return True