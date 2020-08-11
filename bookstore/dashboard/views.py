import json
from datetime import datetime
from .tables import BookTable

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import (
    Topic,
    Language,
    Country,
    Book)

# Create your views here.

def hello(request):
    return render(request, 'dashboard/hello.html')

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

def update_notification_status(request):
    # update book tracking status
    trackingStatus = request.POST['value'] == 'true'
    book = Book.objects.get(id=request.POST['id'])
    book.tracking = trackingStatus
    book.save()

    # change the intervl value if needed
    interval, _ = IntervalSchedule.objects.get_or_create(every=30, period=IntervalSchedule.MINUTES)

    # create or update notification task
    if not PeriodicTask.objects.filter(name='book_' + request.POST['id']).exists():
        notificationTask = PeriodicTask(
            name='book_' + request.POST['id'],
            task='dashboard.tasks.send_notification')
    else:
        notificationTask = PeriodicTask.objects.get(name='book_' + request.POST['id'])

    notificationTask.kwargs = json.dumps({'id': request.POST['id']})
    notificationTask.interval = interval
    notificationTask.enabled = trackingStatus
    notificationTask.save()

    return JsonResponse({'success': True})

class BookListView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'dashboard/book_list.html'
    table_pagination = {
        "per_page": 4
    }