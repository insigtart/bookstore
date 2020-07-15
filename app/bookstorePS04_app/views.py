from django.shortcuts import render

from .models import Carte

# Create your views here.
def index(request):
    return render(request, "carti/filtrare.html", {
        "cărți": Carte.objects.all()
    })

