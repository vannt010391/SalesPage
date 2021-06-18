from django import forms
from django.contrib.messages.api import error
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms.widgets import PasswordInput
from .models import *
import re
from collections import Counter
from django.utils import timezone


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=50, required=False)
    name = forms.CharField(max_length=50)
    messages = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data['email']
        time = timezone.now().date()
        contacts = Contact.objects.filter(email=email, date=time)
        count = 1
        for contact in contacts:
            if(count >= 2):
                raise ValidationError(
                    'Địa chỉ email của bạn đã hết phiên phản hồi. Vui lòng nhập lại')
                break
            else:
                count = count+1
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
            raise ValidationError(
                'Email của bạn không hợp lệ. Vui lòng nhập lại')
        return email

    def clean_name(self):
        name = self.cleaned_data["name"]
        if re.match(r'^\w+$', name):
            print(name)
            raise ValidationError(
                'Tên bạn có chứa kí tự đặt biệt. Vui lòng nhập lại')
        return name


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, required=False)
    username = forms.CharField(
        label='Tên Tài Khoản', max_length=20, min_length=6)
    password1 = forms.CharField(
        label='Mật khẩu', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='Xác nhận mật khẩu', widget=forms.PasswordInput(), min_length=8)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        print(password2)
        raise ValidationError('mật khẩu không hợp lệ')

    def clean_name(self):
        username = self.cleaned_data["username"]
        if not re.match(r'^\w+$', username):
            raise ValidationError(
                'Tên bạn có chứa kí tự đặt biệt. Vui lòng nhập lại')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise ValidationError('Tài khoản đã tồn tại')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise ValidationError('email đã tồn tại')

    def save(self):
        print(1)
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        email=self.cleaned_data['email'],
                                        password=self.cleaned_data['password2'])

class ResetPassForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, required=False)
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise ValidationError('không tìm thấy email')
        return email
        
class ResetPassConfirmForm(forms.Form):
    password1 = forms.CharField(
        label='Mật khẩu', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='Xác nhận mật khẩu', widget=forms.PasswordInput(), min_length=8)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        print(password2)
        raise ValidationError('mật khẩu không hợp lệ')

        

