import imp
from django.urls import path
from notifications.views import showNotifications, DeleteNotification


urlpatterns = [
    path('', showNotifications, name='show-notifications'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification')
]
