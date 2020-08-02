from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views
from dashboard.views import BookSingleTableView
from dashboard.views import BookListView
from dashboard.views import BookDetailView
from dashboard.views import BookTableView

from dashboard.views import BootstrapFilterView

app_name='dashboard'

urlpatterns = [
    path('', views.hello, name='hello'),
    path('index/', views.index, name='index'),
    path('pagina_hello/', views.hello, name='pagina_hello'),
    path('listare_carti/', BookSingleTableView.as_view(), name='book_list'),
    path('list_view_carti/', BookListView.as_view(), name='book_list_view'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
    path('filtrare_carti/',BookTableView.as_view(), name='book_filter'),
    path('book/<str:pk_test>/', views.book, name='book'),
    path('bootstrap_filter_view/', views.BootstrapFilterView, name='bootstrap_filter_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
