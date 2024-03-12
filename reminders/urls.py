# urls.py
from django.urls import path
from .views import create_reminder

urlpatterns = [
    path('create-reminder/', create_reminder, name='create_reminder'),
]
