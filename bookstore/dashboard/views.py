from datetime import datetime
from django.urls import reverse, reverse_lazy

from django.shortcuts import render, redirect
from django_tables2 import SingleTableView
from .tables import BookTable
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView, TemplateView, ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.http import JsonResponse
import json


from .models import Book

from .forms import BookModelForm, EditBookModelForm
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)


class HomeView(TemplateView):
    template_name = "home.html"


class BookListView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'dashboard/book_list.html'
    table_pagination = {
        "per_page": 10
    }


class BookDetailView(DetailView):
    model = Book
    template_name = 'dashboard/book_profile.html'


class BookAddView(CreateView):
    model = Book
    form_class = BookModelForm
    template_name = 'dashboard/book_add.html'
    success_message = "%(title)s was created successfully"
    success_url = reverse_lazy('home')


class BookUpdateView(BSModalUpdateView):
    model = Book
    form_class = EditBookModelForm
    template_name = 'dashboard/book_update.html'
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('home')


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'dashboard/book_delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('home')
    #fields = ['title', 'author', 'description']


def change_book_status(request):
    book = Book.objects.get(id=request.POST['id'])
    book.status = not book.status
    book.save()
    context = {'book': book}
    messages.success(request, "Change status of book: done")
    return render(request, 'dashboard/book_profile.html', context)


def update_notification_status(request):
    # update book tracking status
    trackingStatus = request.POST['value'] == 'true'
    book = Book.objects.get(id=request.POST['id'])
    book.tracking = trackingStatus
    book.save()

    # change the intervl value if needed
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=30, period=IntervalSchedule.MINUTES)

    # create or update notification task
    if not PeriodicTask.objects.filter(name='book_' + request.POST['id']).exists():
        notificationTask = PeriodicTask(
            name='book_' + request.POST['id'],
            task='dashboard.tasks.send_notification')
    else:
        notificationTask = PeriodicTask.objects.get(
            name='book_' + request.POST['id'])

    notificationTask.kwargs = json.dumps({'id': request.POST['id']})
    notificationTask.interval = interval
    notificationTask.enabled = trackingStatus
    notificationTask.save()

    return JsonResponse({'success': True})
