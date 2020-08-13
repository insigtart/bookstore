from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery
from .models import Notification


@shared_task
def send_notification(id):
    Notification.objects.create(
        target=id, name='Cartea ' + id, description='Notificare pentru cartea ' + id)


# @shared_task
# def send_notification():
#     print('Send Notification HEEEREE')
