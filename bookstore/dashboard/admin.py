from django.contrib import admin

from .models import (
    Topic,
    Language,
    Country,
    Book,
    Notification)

# Register your models here.
admin.site.register(Topic)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Book)
admin.site.register(Notification)
