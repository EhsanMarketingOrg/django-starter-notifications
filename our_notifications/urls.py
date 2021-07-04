from django.urls import path
from . import views

app_name = 'our_notifications'
urlpatterns = [
    path('', views.inbox, name='inbox'),
]
