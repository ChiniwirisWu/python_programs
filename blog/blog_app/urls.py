from django.urls import path
from django.urls import include
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_page/', views.createPage, name='create_page'),
    path('remove/<int:id>', views.removePage, name='remove_page'),
    path('read/<int:id>', views.readPage.as_view(), name='read_page'),
]



