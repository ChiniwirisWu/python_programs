from django.urls import path
from . import views

app_name = 'tier_list'

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('/add/', views.addNewPage, name='add'),
]
