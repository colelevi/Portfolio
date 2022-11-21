from django.urls import path 
from . import views

urlpatterns = [
    path('tableau/', views.tableauPageView, name='tableau'),
    path('contact/', views.contactPageView, name='contact'),
    path('about/', views.aboutPageView, name='about'),
    path('', views.indexPageView, name='index'),
]
