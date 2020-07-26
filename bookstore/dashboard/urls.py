from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views
from dashboard.views import BookListView

urlpatterns = [
    path('', views.hello, name='hello'),
    path('pagina_hello/', views.hello, name='pagina_hello'),
    path('listare_carti/', BookListView.as_view(), name='book_list'),
    path('book/<str:pk_test>/', views.book, name='book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
