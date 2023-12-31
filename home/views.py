from django.shortcuts import render
from screenings import models as screeninimodel
from theater import models as theatermodel
from artAndExpriens import models as artandexpriensmodel
from comedyTheater import models as comedytheatermodel
from childrenTheater import models as childrentheatermodel
from salesTable import models as salestablemodel
from news import models as newsadmin


# Create your views here.



def home(request):
    screenings = screeninimodel.Screening.objects.all()
    theaters = theatermodel.Theater.objects.all()
    artandexprienses = artandexpriensmodel.ArtAndExpriens.objects.all()
    comedytheaters = comedytheatermodel.ComedyTheater.objects.all()
    childrentheaters = childrentheatermodel.ChildreTheater.objects.all()
    salestables = salestablemodel.SalesTable.objects.all()
    news = newsadmin.News.objects.all()

    context = {
        "screenings": screenings,
        "theaters":theaters,
        "artandexprienses":artandexprienses,
        "comedytheaters":comedytheaters,
        "childrentheaters":childrentheaters,
        "salestables":salestables,
        "news":news,
        }
    return render(request,"home.html",context)

    
