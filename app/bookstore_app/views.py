from .models import Carte
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

# Create your views here.


def bookslist(request):
    return render(request, "bookstore_app/bookslist.html", {
        "cărți": Carte.objects.all()

    })


def book(request, pk_test):
    book = Carte.objects.get(id=pk_test)
    context = {"book": book}
    return render(request, "bookstore_app/book_card.html", context)
