from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery

@shared_task
def send_notification():
	print('Send Notification HEEEREE')