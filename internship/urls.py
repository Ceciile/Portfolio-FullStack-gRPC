from django.urls import path
from . import views


urlpatterns = [
    path('interns/', views.newinput,name ='newIntern'),
]