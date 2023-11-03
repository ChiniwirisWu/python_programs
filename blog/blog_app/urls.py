from django.urls import path
from django.urls import include
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]



