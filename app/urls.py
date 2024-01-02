from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('events_list',views.event_list, name="event")
]