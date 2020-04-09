from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/data/', views.chart_data, name='chart_data')
]