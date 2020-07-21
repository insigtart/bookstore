from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('book/<str:pk_test>/', views.book, name='book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
