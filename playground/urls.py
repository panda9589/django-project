from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hey),
    path('hello/template', views.say_hey_templates)
]