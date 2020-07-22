from datetime import datetime

from django.shortcuts import render

from .models import (
    Topic,
    Language,
    Country,
    Book)

# Create your views here.


def dashboard(request):
    context = {}

    if request.method == 'POST':
        print(request.POST)
        book = Book.objects.create(title=request.POST['input-title'],
                                   author=request.POST['input-author'],
                                   description=request.POST['input-description'],
                                   datetime=datetime.strptime(request.POST['input-datetime'], '%d.%m.%Y').date())
        print(request.POST)
        book.country.add(Country.objects.get(
            name=request.POST['input-country']))
        book.languages.add(Language.objects.get(
            name=request.POST['input-language']))
        book.topics.add(Topic.objects.get(name=request.POST['input-topic']))

    books = Book.objects.all()
    context['books'] = books
    return render(request, 'dashboard/dashboard.html', context)


def book(request, pk_test):
    book = Book.objects.get(id=pk_test)
    context = {'book': book}
    return render(request, 'dashboard/book_profile.html', context)
