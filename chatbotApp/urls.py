from django.urls import path
from chatbotApp import views
from .views import *

urlpatterns = [
    path('',views.index,name='index'),
]