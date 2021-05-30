from django import forms
from django.core.exceptions import ValidationError
from .models import *
import re
class ContactForm(forms.Form):
    email= forms.EmailField(max_length=50,required=False)
    name = forms.CharField(max_length=50)
    messages = forms.CharField(widget= forms.Textarea)
    def clean_email(self):
        email = self.cleaned_data['email']

        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
            raise ValidationError('Email của bạn không hợp lệ. Vui lòng nhập lại')

        return email
    def clean_name(self):
        name = self.cleaned_data["name"]
        if re.match(r'^\w+$',name):
            raise ValidationError('Tên bạn có chứa kí tự đặt biệt. Vui lòng nhập lại')
            
        return name