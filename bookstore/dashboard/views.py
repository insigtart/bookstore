from datetime import datetime

from django.shortcuts import render

from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django_tables2 import SingleTableView

from django_tables2.config import RequestConfig

from .models import (
    Topic,
    Language,
    Country,
    Book)

from .tables import BookTable
from .filters import BookFilter
from .filters import BookFilterFormHelper

# Create your views here.

from .forms import MessageForm

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'dashboard/index.html', {'form': MessageForm()})


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

def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)


class BookSingleTableView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'dashboard/book_list.html'
    table_pagination = {
        "per_page": 4
    }

class BookListView(ListView):
    model = Book
    template_name = 'dashboard/book_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset = self.get_queryset())
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'dashboard/book_detail_view.html'


def filtrare(request):
    queryset = Book.objects.select_related().all()
    f = BookFilter(request.GET, queryset=queryset)
    table = BookTable(f.qs)
    RequestConfig(request, paginate={'per_page': 4}).configure(table)
    return render(request, 'dashboard/book_filter.html', {'table': table, 'filter': f})

class BookTableView(TemplateView):
    template_name = 'dashboard/book_filter.html'

    def get_queryset(self, **kwargs):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookTableView, self).get_context_data(**kwargs)
        filter = BookFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = BookFilterFormHelper()
        table = BookTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context



def BootstrapFilterView(request):
    return render(request, "dashboard/bootstrap_form.html", {})