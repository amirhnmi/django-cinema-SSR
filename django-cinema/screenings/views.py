from django.shortcuts import render

# Create your views here.

from .models import Screening;

def screening_list(request):
    screenings = Screening.objects.all()
    context = {"screenings": screenings}
    return render(request, "screening/screening.html", context=context)

