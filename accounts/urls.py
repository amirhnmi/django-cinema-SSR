from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),

    path("password_reset/",views.UserPaswordResetView.as_view(),name="password_reset"),
    path("password_reset/done/",views.UserPasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password_reset/confirm/<uidb64>/<token>/",views.UserPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path("password_reset/complate/",views.UserPasswordResetComplateView.as_view(),name="password_reset_complate"),
]