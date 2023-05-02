from django.urls import path
from .views import screening_list

urlpatterns = [
    path("", screening_list, name="screening_list")
]