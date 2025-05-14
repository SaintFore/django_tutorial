from django.urls import path
from . import views

app_name = 'begin'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]