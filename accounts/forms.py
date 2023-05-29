
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=14)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email_input = self.cleaned_data.get("email")
        email_exist = CustomUser.objects.filter(email = email_input).exists()
        if email_exist:
            raise forms.ValidationError("این ایمیل از قبل وجود دارد")
        return email_input
    
    def clean_username(self):
        username_input = self.cleaned_data.get("username")
        username_exist = CustomUser.objects.filter(username = username_input).exists()
        if username_exist:
            raise forms.ValidationError("این نام کاربری قبلا استفاده شده است")
        return username_input
    
    def clean_password2(self):
        password1_input = self.cleaned_data.get("password1")
        password2_input = self.cleaned_data.get("password2")
        if password2_input != password1_input:
            raise forms.ValidationError("کلمه عبور با هم برابر نیستند")
        return password2_input

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email","phone_number")
        
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email","phone_number")
        
