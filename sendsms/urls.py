from .views import *


from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('send-message/', message, name='message'),
]