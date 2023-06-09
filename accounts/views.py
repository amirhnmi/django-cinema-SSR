from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# Create your views here.

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        phone_number = form.cleaned_data.get("phone_number")
        password1 = form.cleaned_data.get("password1")
        CustomUser.objects.create_user(username=username,email=email,password=password1,phone_number=phone_number)
        return redirect("/accounts/login/")
    context={
        "form":form
    }
    return render(request,"accounts/register.html",context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "GET":
        form = LoginForm()
    elif request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("/")
            form.add_error("email", "ایمیل یا رمزعبور نادرست است")
            form.add_error("password", "ایمیل یا رمزعبور نادرست است")
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def dashboard_view(request):
    return render(request, "dashboard/user_dashboard.html")


# password reset --------------
class UserPaswordResetView(PasswordResetView):
    template_name = "password_reset/password_reset.html"
    email_template_name = "password_reset/password_reset_email.html"
    html_email_template_name= "password_reset/password_reset_email_template.html"
    subject_template_name = "password_reset/password_reset_subject.txt"
    from_email = "mr.arhnmi@gmail.com"
    success_url = reverse_lazy("accounts:password_reset_done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "password_reset/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complate")


class UserPasswordResetComplateView(PasswordResetCompleteView):
    template_name = "password_reset/password_reset_complate.html"