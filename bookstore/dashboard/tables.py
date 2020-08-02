import django_tables2 as tables
from django_tables2.columns import TemplateColumn

from .models import Book

class BookTable(tables.Table):    
    select = TemplateColumn('<input type="checkbox" value="{{ record.pk }}" />', verbose_name=" ")
    view = TemplateColumn(template_code='<a class="btn btn-sm btn-info" href="{% url "dashboard:book" record.id %}">Fișă</a>', verbose_name=" ")
    
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ("select", "id", "title", "author", "languages", "topics", "description", "view")
    
    