from django.shortcuts import render
from .models import Carte

# Create your views here.


def home(request):
    return render(request, 'home.html')


# Create your views here.
def index(request):
    return render(request, "bookstore_app/listare_carti.html", {
        "cărți": Carte.objects.all()

    })
