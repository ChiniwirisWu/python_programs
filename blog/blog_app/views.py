from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return models.Page.objects.all()

class readPage(generic.ListView):
    template_name = 'page.html'
    context_object_name = 'page'
    model = models.Page

    def get_queryset(self):
        return model.objects.get(pk=request.GET['id'])

def createPage(request):
    model = models.Page
    description = request.POST['content'][:10] + "..."
    page = model(title = request.POST['title'], content = request.POST['content'], pub_date = timezone.now(), description=description)
    page.save()
    return HttpResponseRedirect(reverse('blog_app:index'))


def removePage(request):
    pass
