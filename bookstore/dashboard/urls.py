from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/create/', views.BookAddView.as_view(), name='create_book'),
    path('books/read/<int:pk>/', views.BookDetailView.as_view(), name='read_book'),
    path('books/update/<int:pk>/',
         views.BookUpdateView.as_view(), name='update_book'),
    path('books/delete/<int:pk>/',
         views.BookDeleteView.as_view(), name='delete_book'),
    path('change_book_status/', views.change_book_status,
         name='change_book_status'),
    path('update_notification_status', views.update_notification_status,
         name='update_notification_status'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
